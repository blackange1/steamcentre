from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from steamcentre.settings import PAGE_SIZE
from .models import EduMaterial, EduСategory, Color
from .serializers import OneEduMaterialSerializer, ColorSerializer


def show_material(request):
    return render(request, 'methodical_material/material.html')


def show_own_material(request, pk):
    edu_material = EduMaterial.objects.filter(pk=pk)
    if edu_material:
        return render(request, 'methodical_material/own_material.html', context={'pk': pk})
    return redirect('show_material')


class ColorSerializerAPIView(APIView):
    def get(self, request, pk):
        colors = Color.objects.filter(id=pk)
        if colors:
            color = colors[0]
            return Response(ColorSerializer(color).data)
        return Response()


class EduMaterialAPIView(APIView):
    """
    API endpoint that allows edu materia to be viewed or edited.
    """

    @staticmethod
    def __get_dict_edu_material(obj, all_matirial=False, one_material=False):
        is_favorite = False
        is_liked = False
        if all_matirial:
            try:
                matirial = EduMaterial.objects.get(pk=obj.pk)
                if matirial in all_matirial[0]:
                    is_favorite = True
                if matirial in all_matirial[1]:
                    is_liked = True
            except:
                pass

        edu_сategory = [c.name for c in obj.edu_сategory.all()]
        description = [s for s in obj.description.split('\r\n')]

        res = {
            'id': obj.id,
            'name': obj.name,
            'edu_сategory': edu_сategory,
            'color': obj.color.color,
            'img': obj.img.url,
            'description': description,
            'link_download': obj.link_download,
            'source': obj.source,
            'like': obj.like,
            'count_comments': obj.count_comments,
            'is_favorite': is_favorite,
            'is_liked': is_liked,
        }

        if one_material:
            res.update({'detailed_description': obj.detailed_description})

        return res

    @staticmethod
    def __get_response_pagination(lst, page=1, page_size=PAGE_SIZE):
        end_position = page * page_size
        count_page = len(lst) // page_size + int(bool(len(lst) % page_size))
        if count_page < page:
            return []
        return {
            'count_page': count_page,
            'page': page,
            'matirial': lst[end_position - page_size:end_position]
        }

    def get(self, request, pk=None):
        page = 1
        try:
            page = int(dict(request.query_params).get('page', [1])[0])
        except:
            pass

        print(page, type(page))

        all_matirial = False
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            all_matirial = []
            all_matirial.append(profile.collection_material.all())
            all_matirial.append(profile.liked.all())

        # pass instants pk
        if pk:
            materials = EduMaterial.objects.filter(pk=pk)
            if materials:
                m = materials[0]
                return Response(
                    self.__get_dict_edu_material(m, all_matirial, True)
                )

        lst = []

        # ?filer='favorite'
        filer = dict(request.query_params).get('filer', None)
        print(filer)
        if filer:
            filer = filer[0]
            user = request.user
            index = 0
            if filer == 'liked':
                index = 1

            if filer in ('favorite', 'liked') and not(user.is_anonymous):
                if hasattr(user, 'profile'):
                    # for edu_material in user.profile.collection_material.all():
                    for edu_material in all_matirial[index]:
                        lst.append(self.__get_dict_edu_material(edu_material, all_matirial))
            return Response(self.__get_response_pagination(lst, page))

        # ?categories=3D&categories=Tinkercad
        set_id = set()
        list_category = dict(request.query_params).get('categories', None)
        if list_category:
            list_category = list_category[0].split(',')
            print('list_category', list_category)
            for category in list_category:
                for edu_material in EduMaterial.objects.filter(edu_сategory__name=category):
                    if edu_material.id in set_id:
                        continue
                    set_id.add(edu_material.id)
                    lst.append(self.__get_dict_edu_material(edu_material, all_matirial))
            return Response(self.__get_response_pagination(lst, page))

        # ?words=3
        words = dict(request.query_params).get('words', None)
        if words:
            words = words[0]
            words = words.strip()
            q_name = EduMaterial.objects.filter(name__contains=words)
            q_description = EduMaterial.objects.filter(description__contains=words)
            q_set = set(q_name)
            q_set.update(q_description)
            for edu_material in q_set:
                lst.append(self.__get_dict_edu_material(edu_material, all_matirial))
            return Response(self.__get_response_pagination(lst, page))

        for edu_material in EduMaterial.objects.all():
            lst.append(self.__get_dict_edu_material(edu_material, all_matirial))

        self.__get_response_pagination(lst)
        return Response(self.__get_response_pagination(lst, page))


class EduСategoryAPIView(APIView):
    def get(self, request):
        lst = EduСategory.objects.all().order_by('name').values()
        return Response({'category': list(lst)})

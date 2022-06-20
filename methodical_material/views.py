from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

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
    def __get_dict_edu_material(obj, all_matirial=False):
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

        return {
            'id': obj.id,
            'name': obj.name,
            'edu_сategory': edu_сategory,
            'color': obj.color.color,
            'img': obj.img.url,
            'description': description,
            'link_download': obj.link_download,
            'source': obj.source,
            'like': obj.like,
            'is_favorite': is_favorite,
            'is_liked': is_liked,
        }

    def get(self, request, pk=None):
        # pass instants pk
        if pk:
            materials = EduMaterial.objects.filter(id=pk)
            if materials:
                m = materials[0]
                return Response(
                    OneEduMaterialSerializer(m).data
                )
            return Response({'error': 'not fined'})

        lst = []

        all_matirial = False
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            all_matirial = []
            all_matirial.append(profile.collection_material.all())
            all_matirial.append(profile.liked.all())

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
            return Response({'matirial': lst})

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
            return Response({'matirial': lst})

        for edu_material in EduMaterial.objects.all():
            lst.append(self.__get_dict_edu_material(edu_material, all_matirial))

        return Response({'matirial': lst})


class EduСategoryAPIView(APIView):
    def get(self, request):
        lst = EduСategory.objects.all().order_by('name').values()
        return Response({'category': list(lst)})

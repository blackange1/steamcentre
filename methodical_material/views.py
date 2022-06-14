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


class OneEduMaterialAPIView(APIView):
    def get(self, request, pk):
        materials = EduMaterial.objects.filter(id=pk)
        if materials:
            m = materials[0]
            return Response(OneEduMaterialSerializer(m).data)
        return Response()


class EduMaterialAPIView(APIView):
    """
    API endpoint that allows edu materia to be viewed or edited.
    """

    @staticmethod
    def __get_dict_edu_material(obj):
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
        }

    def get(self, request):
        lst = []
        for edu_material in EduMaterial.objects.all():
            lst.append(self.__get_dict_edu_material(edu_material))
        return Response({'matirial': lst})

    def post(self, request):
        lst = []

        # body: b"{'categories': ...}"
        set_id = set()
        list_category = request.data.get('categories', None)
        if not (list_category is None):
            for category in list_category:
                for edu_material in EduMaterial.objects.filter(edu_сategory__name=category):
                    if edu_material.id in set_id:
                        continue
                    set_id.add(edu_material.id)
                    lst.append(self.__get_dict_edu_material(edu_material))

        # body: b"{'words': ...}"
        words = request.data.get('words', None)
        if words != None:
            words = words.strip()
            q_name = EduMaterial.objects.filter(name__contains=words)
            q_description = EduMaterial.objects.filter(description__contains=words)
            q_set = set(q_name)
            q_set.update(q_description)
            for edu_material in q_set:
                lst.append(self.__get_dict_edu_material(edu_material))

        return Response({'matirial': lst})


class EduСategoryAPIView(APIView):
    def get(self, request):
        lst = EduСategory.objects.all().order_by('name').values()
        return Response({'category': list(lst)})

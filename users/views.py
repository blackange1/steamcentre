from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .models import Profile
from steamcentre.settings import BASE_DIR, MEDIA_ROOT
from methodical_material.models import EduMaterial


def user_info(request, username):
    if not request.user.is_active or username != request.user.username:
        return redirect('index')

    profile = list(Profile.objects.filter(user_id=request.user.id))
    if profile:
        profile = profile[0]
    else:
        profile = None

    massages = []
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.save()
        if request.FILES:
            if profile:
                path_img = profile.img.url.split('/')[-1]
                BASE_DIR.joinpath(MEDIA_ROOT).joinpath('user_photos').joinpath(path_img).unlink()
                profile.delete()

            Profile.objects.create(user=request.user, img=request.FILES['img'])
            massages.append('Фото завантажується. Перезавантажте сторінку')

        url_photo = ''
        if profile:
            url_photo = profile.img.url
        
        massages.append('Дані збережено')
        return render(request, 'users/user_info.html', context={'url_photo': url_photo, 'massages': massages})

    url_photo = ''
    if profile.img:
        url_photo = profile.img.url
    return render(request, 'users/user_info.html', context={'url_photo': url_photo, 'massages': massages})


class ProfileAPIView(APIView):
    def get(self, request):
        query_profile = Profile.objects.filter(user_id=request.user.id)
        if query_profile:
            profile = query_profile[0]
            query_collection_material = profile.collection_material.filter()
            context = {
                'collection_materials_id': [obj.pk for obj in query_collection_material]
            }

            return Response(context)
        return Response({'error': 'is not authorization'})

    def put(self, request):
        if request.user.is_anonymous:
            return Response({'error': 'is_anonymous'})

        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)

        def add_or_remove(material, all_material, profile_property):
            if material in all_material:
                profile_property.remove(material)
                return False
            profile_property.add(material)
            return True

        profile = request.user.profile

        pk = request.data.get('favorite_id', None)
        key_d = 'favorite_id'
        if not pk:
            pk = request.data.get('like_id', None)
            key_d = 'like_id'

        try:
            material = EduMaterial.objects.get(pk=pk)
        except:
            return Response({'error': 'error pk'})

        all_material = profile.collection_material.all() if key_d == 'favorite_id' else profile.liked.all()
        profile_property = profile.collection_material if key_d == 'favorite_id' else profile.liked
        is_add = add_or_remove(material, all_material, profile_property)
        if key_d == 'like_id':
            if is_add:
                material.like += 1
            else:
                material.like -= 1
            material.save()

        return Response({'response': 'good'})

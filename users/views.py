from django.shortcuts import render, redirect
from .models import Profile
from steamcentre.settings import BASE_DIR, MEDIA_ROOT


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

    if profile:
        url_photo = profile.img.url

    return render(request, 'users/user_info.html', context={'url_photo': url_photo, 'massages': massages})

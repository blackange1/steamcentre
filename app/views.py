from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from app.forms import LoginForm
from app.models import MainSlider


def index(request):
    print(MainSlider.objects.all())
    return render(request,
                  'app/index.html',
                  {
                      'cards': MainSlider.objects.all()
                  })


def login_user(request):
    if request.user.is_active:
        return redirect(index)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                request, username=username, password=password
            )
            print(password)
            if user is not None:
                login(request, user)
                return redirect(index)
            return render(
                request,
                'app/auth/login.html',
                {
                    'form': LoginForm,
                    'message': 'пароль або логін не вірні'
                }
            )
        return render(
            request,
            'app/auth/login.html',
            {
                'form': LoginForm,
                'message': 'видопустили помилки пи заповнені форми, спробуйте ще раз'
            }
        )
    return render(
        request,
        'app/auth/login.html',
        {'form': LoginForm, 'message': ''}
    )

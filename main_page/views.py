from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from main_page.forms import LoginForm, NewUserForm
from main_page.models import MainSlider


def error_404(request, *args, **argv):
    return render(request, 'main_page/404.html')


def error_500(request, *args, **argv):
    return render(request, 'main_page/500.html')


def index(request):
    return render(request, 'main_page/index.html', {'cards': MainSlider.objects.all()})


def faq(request):
    return render(request, 'main_page/faq.html')


# def login_user(request):
#     if request.user.is_active:
#         return redirect(index)
#     context = {
#         'form': LoginForm,
#         'message': ''
#     }
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect(index)
#             context['message'] = 'пароль або логін не вірні'
#             return render(request, 'main_page/auth/login.html', context)
#         context['message'] = 'ви допустили помилки пи заповнені форми, спробуйте ще раз'
#         return render(request, 'main_page/auth/login.html', context)
#     return render(request, 'main_page/auth/login.html', context)
#
#
# def register_request(request):
#     if request.user.is_active:
#         return redirect(index)
#     context = {
#         "register_form": NewUserForm(),
#         'message': '',
#     }
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#
#         if form.is_valid():
#             username = request.POST['username']
#
#             if User.objects.filter(username=username):
#                 context['message'] = "Користувач з таким ім'ям уже існує"
#                 return render(request, "main_page/auth/register.html", context)
#
#             email = request.POST['email']
#             if User.objects.filter(email=email):
#                 context['message'] = "Користувач з такою поштою вже існує"
#                 return render(request, "main_page/auth/register.html", context)
#
#             pw1 = request.POST['pw1']
#             pw2 = request.POST['pw2']
#             if pw1 != pw2:
#                 context['message'] = "Паролі неспівпадають"
#                 return render(request, "main_page/auth/register.html", context)
#
#             if len(pw1) < 8:
#                 context['message'] = "Пароль менше 8-ми символів"
#                 return render(request, "main_page/auth/register.html", context)
#
#             user = User.objects.create_user(username, email, pw1)
#             login(request, user)
#             return redirect(index)
#
#     return render(request, "main_page/auth/register.html", context)
#
#
# def logout_user(request):
#     if not request.user.is_active:
#         return redirect(index)
#     logout(request)
#     return render(request, "main_page/auth/logout.html")



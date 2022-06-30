from django.urls import path

from .views import index, faq

# from .views import index, login_user, register_request, logout_user

urlpatterns = [
    path('', index, name='index'),
    path('faq/', faq, name='faq'),
]

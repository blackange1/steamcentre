from django.urls import path

from .views import index

# from .views import index, login_user, register_request, logout_user

urlpatterns = [
    path('', index, name='index'),
    # path('login/', login_user, name='login'),
    # path('register/', register_request, name='register'),
    # path('logout/', logout_user, name='logout'),
    # path('accounts/profile/', profile, name='profile')
]

from django.urls import path

from .views import index, create_cat_main_slider

urlpatterns = [
    path('', index, name='index'),
    path('create_cat_main_slider/', create_cat_main_slider, name='create_cat_main_slider')
]

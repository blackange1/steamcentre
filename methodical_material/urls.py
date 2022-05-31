from django.urls import path
from .views import show_material

urlpatterns = [
    path('', show_material, name='show_material'),
]

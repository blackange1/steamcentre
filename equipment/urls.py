from django.urls import path
from .views import equipment

urlpatterns = [
    path('', equipment, name='equipment'),
]


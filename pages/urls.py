from django.urls import path
from .views import get_page

urlpatterns = [
    path('<slug:slug>', get_page, name='page'),
]

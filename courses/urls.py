from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import show_curses

urlpatterns = [
    path('', show_curses, name='curses')

]

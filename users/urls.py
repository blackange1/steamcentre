from django.urls import path
from .views import user_info

urlpatterns = [
    path('<username>/', user_info, name='user_info')
]

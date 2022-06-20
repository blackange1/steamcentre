from django.urls import path
from .views import user_info, ProfileAPIView

urlpatterns = [
    path('user/<username>/', user_info, name='user_info'),
    path('user/<username>/', user_info, name='user_info'),
    path('api/v1/user/', ProfileAPIView.as_view()),
]

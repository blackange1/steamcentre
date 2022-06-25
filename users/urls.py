from django.urls import path
from .views import user_info, ProfileAPIView, CommentsAPIView

urlpatterns = [
    path('user/<username>/', user_info, name='user_info'),
    path('api/v1/user/', ProfileAPIView.as_view()),
    path('api/v1/edumaterials/<int:pk_material>/comments/', CommentsAPIView.as_view()),
    path('api/v1/edumaterials/<int:pk_material>/comments/<int:pk_comment>', CommentsAPIView.as_view()),
    path('api/v1/edumaterials/<int:pk_material>/comments/<int:pk_comment>/<int:pk_sub_comment>', CommentsAPIView.as_view()),
]

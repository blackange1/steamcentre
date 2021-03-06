from django.urls import path, include
from .views import show_material, EduMaterialAPIView, EduСategoryAPIView,\
    show_own_material, ColorSerializerAPIView
# from .views import email


urlpatterns = [
    # path('email/', email, name='email'),
    path('api/v1/edumaterials/', EduMaterialAPIView.as_view()),
    path('api/v1/edumaterials/<int:pk>', EduMaterialAPIView.as_view()),
    path('api/v1/categories/', EduСategoryAPIView.as_view()),
    path('api/v1/color/<int:pk>', ColorSerializerAPIView.as_view()),
    path('methodical_material/', show_material, name='show_material'),
    path('methodical_material/<int:pk>', show_own_material, name='show_own_material'),
]

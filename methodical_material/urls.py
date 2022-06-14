from django.urls import path, include
from .views import show_material, EduMaterialAPIView, EduСategoryAPIView,\
    show_own_material, OneEduMaterialAPIView,ColorSerializerAPIView
from rest_framework import routers

#
# router = routers.DefaultRouter()
# router.register(r'material', EduMaterialViewSet)


urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/v1/edumaterials/', EduMaterialAPIView.as_view()),
    path('api/v1/edumaterials/<int:pk>', OneEduMaterialAPIView.as_view()),
    path('api/v1/categories/', EduСategoryAPIView.as_view()),
    path('api/v1/color/<int:pk>', ColorSerializerAPIView.as_view()),
    path('methodical_material/', show_material, name='show_material'),
    path('methodical_material/<int:pk>', show_own_material, name='show_own_material'),
]

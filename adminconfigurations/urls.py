from django.urls import path
from .views import CropViewSet, FarmTypeViewSet, FarmerDataViewSet


urlpatterns = [
    path('crop/', CropViewSet.as_view({'get': 'list', 'post': 'create'}), name='crops'),
    path('farmtype/', FarmTypeViewSet.as_view({'get': 'list', 'post': 'create'}), name='farm types'),
    path('farmers/', FarmerDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='farmer details'),
]

from rest_framework import viewsets
from .models import AdminConfigurationFarmType, AdminConfigurationCrop, FarmerData
from .serializers import CropSerializer, FarmTypeSerializer, FarmerDataSerializer
from .permissions import IsAdminUser, IsClerkUser

class CropViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return AdminConfigurationCrop.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsClerkUser | IsAdminUser]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    serializer_class = CropSerializer
    permission_classes = [IsAdminUser]

class FarmTypeViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return AdminConfigurationFarmType.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsClerkUser | IsAdminUser]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    serializer_class = FarmTypeSerializer
    permission_classes = [IsAdminUser]

class FarmerDataViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return FarmerData.objects.all()
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsClerkUser | IsAdminUser]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    serializer_class = FarmerDataSerializer
    permission_classes = [IsClerkUser]
    
    

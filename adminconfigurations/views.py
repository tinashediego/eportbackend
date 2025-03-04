from rest_framework import viewsets
from .models import AdminConfigurationFarmType, AdminConfigurationCrop, FarmerData
from .serializers import CropSerializer, FarmTypeSerializer, FarmerDataSerializer
from .permissions import IsAdminUser, IsClerkUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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
    
class FarmerDataViewSet(viewsets.ModelViewSet):
    # existing methods

    @action(detail=False, methods=['post'], permission_classes=[IsClerkUser])
    def sync(self, request):
        data = request.data
        # Perform sync operation here
        # For example, you can iterate over the data and save it to the database
        for item in data:
            FarmerData.objects.update_or_create(
                id=item.get('id'),
                defaults=item
            )
        return Response({'status': 'sync successful'}, status=status.HTTP_200_OK)


from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, permissions
from .models import FarmerData
from .serializers import FarmerDataSerializer

# Views
class FarmerDataViewSet(viewsets.ModelViewSet):
    queryset = FarmerData.objects.all()
    serializer_class = FarmerDataSerializer
    permission_classes = [permissions.IsAuthenticated]


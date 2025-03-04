
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, permissions
from .models import Config
from .serializers import ConfigSerializer

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    permission_classes = [permissions.IsAuthenticated]


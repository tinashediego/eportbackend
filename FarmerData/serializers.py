from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import FarmerData

class FarmerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerData
        fields = '__all__'


from rest_framework import serializers
from .models import FarmerData, AdminConfigurationFarmType, AdminConfigurationCrop

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminConfigurationCrop
        fields = '__all__'

class FarmTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminConfigurationFarmType
        fields = '__all__'

class FarmerDataSerializer(serializers.ModelSerializer):
    crop = serializers.PrimaryKeyRelatedField(queryset=AdminConfigurationCrop.objects.all(), required=True)
    farm_type = serializers.PrimaryKeyRelatedField(queryset=AdminConfigurationFarmType.objects.all(), required=True)

    class Meta:
        model = FarmerData
        fields = '__all__'
        depth = 1


from django.db import models

class AdminConfigurationCrop(models.Model):
    id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=255)
    def __str__(self):
        return f"Admin Configuration for {self.crop_type_name}"

class AdminConfigurationFarmType(models.Model):
    id = models.AutoField(primary_key=True)
    farm_type_name = models.CharField(max_length=255)
    def __str__(self):
        return f"Admin Configuration for {self.farm_type_name}"

class FarmerData(models.Model):
    farmer_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=20)
    farm_type = models.ForeignKey(AdminConfigurationFarmType, on_delete=models.CASCADE, null=True, blank=True)
    crop = models.ForeignKey(AdminConfigurationCrop, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.farmer_name
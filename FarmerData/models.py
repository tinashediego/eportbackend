from django.db import models
from django.contrib.auth.models import User
# Farmer Data Model
class FarmerData(models.Model):
    farmer_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=50, unique=True)
    farm_type = models.CharField(max_length=100)
    crop = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.farmer_name


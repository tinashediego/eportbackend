
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


# Configurations for Admin Role
class Config(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    
    def __str__(self):
        return self.name


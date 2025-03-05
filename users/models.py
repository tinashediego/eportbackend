import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('clerk', 'Clerk'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='clerk')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role', 'first_name', 'last_name']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'role': self.role,  # Include the role in the token
        }

from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    """ Register a new user """
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role', 'clerk')  # Default role is 'clerk'

    if not email or not username or not password:
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(email=email, username=username, password=password, role=role)
    return Response({'tokens': user.tokens(), 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)

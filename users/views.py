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
    """ Register a new user (default role is Clerk) """
    role = request.data.get('role', 'clerk')  # Default role is clerk
    if role not in ['admin', 'clerk']:
        return Response({'error': 'Invalid role'}, status=400)

    user = get_user_model().objects.create_user(
        email=request.data['email'],
        username=request.data['username'],
        password=request.data['password']
    )

    # Set role manually since `create_user` does not accept it
    user.role = role
    user.save()

    return Response({'tokens': user.tokens()})


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_by_id(request, user_id):
    """ Retrieve a user by their ID """
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
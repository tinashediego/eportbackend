from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register, get_user_by_id

urlpatterns = [
    path('register/', register, name='register'),
    path('user/<str:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

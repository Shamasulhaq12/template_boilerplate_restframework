from django.urls import path
from core.views import RegistrationView, ForgetPasswordView, UserDetailView, ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgetpassword/', ForgetPasswordView.as_view(), name='forgetpassword'),
    path('me/', UserDetailView.as_view(), name='user'),
    path('changepassword/', ChangePasswordView.as_view(), name='changepassword'),

]

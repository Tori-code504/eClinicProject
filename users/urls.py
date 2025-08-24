from django.urls import path
from .views import RegisterView, user_profile
from .views import RegisterView, LogoutView, CurrentUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("profile/", user_profile, name="user_profile"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", CurrentUserView.as_view(), name="current-user"),
]
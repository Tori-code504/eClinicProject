from django.urls import path
from .views import CustomTokenObtainPairView, RegisterView, UserListView
from .views import RegisterView, LogoutView, CurrentUserView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView # type: ignore

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", CurrentUserView.as_view(), name="current-user"),
    path("", UserListView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("logout/", LogoutView.as_view(), name="logout"),
   
]
from django.urls import path
from .views import RegisterView, user_profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("profile/", user_profile, name="user_profile"),
]
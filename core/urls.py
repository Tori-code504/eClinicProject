from django.urls import path
from .views import RegisterView, UserListView, PatientProfileView
from django.urls import path, include

urlpatterns =[
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('patient/profile/',PatientProfileView.as_view(), name='patient-profile'),
]
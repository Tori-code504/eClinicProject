from django.urls import path
from .views import PatientProfileListCreateView, PatientProfileDetailView

urlpatterns = [
    path("", PatientProfileListCreateView.as_view(), name="patientprofile-list-create"),
    path("<int:pk>/", PatientProfileDetailView.as_view(), name="patientprofile-detail"),
]
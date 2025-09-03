from django.urls import path
from .views import PatientProfileListCreateView, PatientProfileDetailView

urlpatterns = [
    path("patients/", PatientProfileListCreateView.as_view(), name="patient-list-create"),
    path("patients/<int:pk>/", PatientProfileDetailView.as_view(), name="patient-detail"),
]
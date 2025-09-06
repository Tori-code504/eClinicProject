from django.urls import path
from .views import PatientProfileListCreateView, PatientProfileDetailView

urlpatterns = [
    path("profiles/", PatientProfileListCreateView.as_view(), name="patientprofile-list-create"),
    path("profiles/<int:pk>/", PatientProfileDetailView.as_view(), name="patientprofile-detail"),
]
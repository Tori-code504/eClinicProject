from django.urls import path
from .views import MedicalRecordListCreateView, MedicalRecordDetailView

urlpatterns = [
    path("", MedicalRecordListCreateView.as_view(), name="medicalrecord-list-create"),
    path("<int:pk>/", MedicalRecordDetailView.as_view(), name="medicalrecord-detail"),
]

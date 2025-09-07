from django.urls import path
from .views import MedicalRecordListCreateView, MedicalRecordDetailView

urlpatterns = [
    path("", MedicalRecordListCreateView.as_view(), name="record-list"),
    path("<int:pk>/", MedicalRecordDetailView.as_view(), name="record-detail"),
]

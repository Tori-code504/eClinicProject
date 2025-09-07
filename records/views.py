from rest_framework import generics, permissions
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
from core.permissions import IsDoctorOrAdminOrOwner


class BaseMedicalRecordView:
    """Shared queryset logic for MedicalRecord views."""

    def get_queryset(self):
        user = self.request.user
        if user.role in ["Doctor", "Admin"]:
            return MedicalRecord.objects.all()
        # Patients only see their own records
        return MedicalRecord.objects.filter(patient__user=user)


class MedicalRecordListCreateView(BaseMedicalRecordView, generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorOrAdminOrOwner]

    def perform_create(self, serializer):
        """Only Doctors and Admins can create records."""
        if self.request.user.role not in ["Doctor", "Admin"]:
            raise permissions.PermissionDenied("Only Doctors or Admins can create medical records.")
        serializer.save()


class MedicalRecordDetailView(BaseMedicalRecordView, generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorOrAdminOrOwner]

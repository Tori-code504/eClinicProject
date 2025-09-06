from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied, ValidationError
from .models import PatientProfile
from .serializers import PatientProfileSerializer
from .permissions import IsAdminOrOwner


class PatientProfileListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "Admin":
            return PatientProfile.objects.all()
        return PatientProfile.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != "Patient":
            raise PermissionDenied("Only patients can create their own profile.")
        if hasattr(user, "patient_profile"):
            raise ValidationError("This user already has a PatientProfile.")
        serializer.save(user=user)


class PatientProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

from rest_framework import generics, permissions
from .models import PatientProfile
from .serializers import PatientProfileSerializer
from core.permissions import IsAdminOrOwner

class PatientProfileListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "Admin":
            return PatientProfile.objects.all()
        return PatientProfile.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PatientProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]


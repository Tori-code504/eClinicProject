from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer
from patients.models import PatientProfile

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "Admin":
            return Appointment.objects.all()
        if user.role == "Doctor":
            return Appointment.objects.filter(doctor=user)
        if user.role == "Patient":
            return Appointment.objects.filter(patient=user.patient_profile)
        return Appointment.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role == "Patient":
            patient_profile = self.request.user.patient_profile
            serializer.save(patient=patient_profile)
        else:
            raise PermissionError("Only patients can create appointments.")


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "Admin":
            return Appointment.objects.all()
        if user.role == "Doctor":
            return Appointment.objects.filter(doctor=user)
        if user.role == "Patient":
            return Appointment.objects.filter(patient=user.patient_profile)
        return Appointment.objects.none()


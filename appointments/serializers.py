from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'service_type', 'appointment_time', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']
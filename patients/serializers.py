from rest_framework import serializers
from .models import PatientProfile

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['id', 'user', 'date_of_birth', 'gender', 'id_number', 'address']
        read_only_fields = ['id', 'user']
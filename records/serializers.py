from rest_framework import serializers
from .models import MedicalRecord

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"

    def validate(self, attrs):
        user = self.context["request"].user
        method = self.context["request"].method

        # Patients should not create or modify
        if user.role == "Patient" and method not in ["GET", "HEAD", "OPTIONS"]:
            raise serializers.ValidationError(
                "Only Doctors and Admins can create or edit medical records. Patients may only view their own records."
            )

        # Nurses should also not create/edit records
        if user.role == "Nurse" and method not in ["GET", "HEAD", "OPTIONS"]:
            raise serializers.ValidationError(
                "Nurses are not allowed to create or edit medical records. Only Doctors and Admins can."
            )

        return attrs


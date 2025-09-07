from rest_framework import serializers
from .models import PatientProfile

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['id', 'user', 'date_of_birth', 'gender', 'id_number', 'address']
        read_only_fields = ['id', 'user']

    def validate(self, data):
        user = self.context["request"].user

        # Only patients can create a profile
        if user.role != "Patient":
            raise serializers.ValidationError("Only patients can create their own profile.")

        # Prevent duplicate profiles
        if self.instance is None and PatientProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError("This user already has a PatientProfile.")

        return data

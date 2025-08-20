from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PatientProfile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username' , 'role', 'email', 'phone_number']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email= validated_data.get('email'),
            phone_number = validated_data.get('phone_number'),
            role = validated_data.get('role'),
            password= validated_data['password']
        )
        return user
    
class PatientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PatientProfile
        fields = ['id', 'user', 'date_of_birth', 'gender', 'national_id', 'address']
from rest_framework import serializers
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields =['id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email'),
            password = validated_data['password'],
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', ''),
            phone_number = validated_data.get('phone_number', ''),
            role = validated_data.get('role', 'Patient'),
        )
        return user 

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # only return safe fields (not password, etc.)
        fields = ["id", "username", "email", "first_name", "last_name"]


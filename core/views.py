from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import PatientProfile
from .serializers import UserSerializer, RegisterSerializer, PatientProfileSerializer

User = get_user_model()

#Register new User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

#List all users(only for admins)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

#Patient profile CRUD
class PatientProfileView(generics.RetrieveUpdateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.patient_profile

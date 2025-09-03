from django.shortcuts import render
from rest_framework import generics, permissions
from .models import PatientProfile
from .serializers import PatientProfileSerializer
from .permissions import IsAdminOrOwner

class PatientProfileListCreateView(generics.ListCreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Admin':
            return PatientProfile.objects.all()
        return PatientProfile.objects.filter(user=user)
    
    def perform_create(self, serializer):
        if self.request.user.role == 'Patient':
            serializer.save(user=self.request.user)
        else:
            raise PermissionError ('Only Patients can create their own Profile.')
        

class PatientProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]
    
       

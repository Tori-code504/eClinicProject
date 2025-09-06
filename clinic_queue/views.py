from django.shortcuts import render
from rest_framework import generics
from .models import QueueEntry
from .serializers import QueueSerializer

class QueueListView(generics.ListCreateAPIView):
    queryset = QueueEntry.objects.all()
    serializer_class = QueueSerializer


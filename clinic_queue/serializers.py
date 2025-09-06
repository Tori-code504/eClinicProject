from rest_framework import serializers
from .models import QueueEntry

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueEntry
        fields = "__all__"

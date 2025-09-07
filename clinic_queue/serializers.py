from rest_framework import serializers
from .models import QueueEntry

class QueueEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueEntry
        fields = "__all__"

    def validate(self, attrs):
        user = self.context["request"].user
        if user.role == "Patient" and self.context["request"].method not in ["GET", "HEAD", "OPTIONS"]:
            raise serializers.ValidationError(
                "Only Admins and Nurses can manage the queue. Patients may only view their own entries."
            )
        return attrs

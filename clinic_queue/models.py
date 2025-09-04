from django.db import models
from django.conf import settings
from appointments.models import Appointment

class QueueEntry(models.Model):
    appointment = models.OneToOneField(
        Appointment, on_delete=models.CASCADE, related_name='queue_entry'
    )
    position = models.PositiveIntegerField()
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Queue #{self.position} - {self.appointment.patient.username}"

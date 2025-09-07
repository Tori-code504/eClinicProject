from django.db import models
from django.conf import settings
from appointments.models import Appointment

class QueueEntry(models.Model):
    appointment = models.OneToOneField(
        Appointment, on_delete=models.CASCADE, related_name='queue_entry'
    )
    position = models.PositiveIntegerField()
    status = models.CharField(
        max_length= 20,
        choices=[('waiting', 'Waiting'), 
                 ('called', 'Called'), 
                 ('completed', 'Completed')
                 ],
        default="waiting"

    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.appointment.patient.user.username} - {self.status}"

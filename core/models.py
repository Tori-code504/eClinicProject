from django.db import models
from django.conf import settings
from appointments.models import Appointment

class QueueEntry(models.Model):

    appointment = models.OneToOneField('appointments.Appointment', on_delete= models.CASCADE, related_name= 'queue_entry')
    position = models.PositiveIntegerField()  
    time_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Queue #{self.position} - {self.appointment.patient.username}" 
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="medical_records")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="created_records")
    record_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Record for {self.patient.username} on {self.record_date}"



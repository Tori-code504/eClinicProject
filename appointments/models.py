from django.db import models
from django.conf import settings
from patients.models import PatientProfile

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name='appointments'
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.SET_NULL,
        null= True,
        blank=True,
        limit_choices_to={'role':'Doctor'},
        related_name='appointments'

    )
    service_type =models.CharField(max_length=100)
    appointment_time = models.DateTimeField()
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.patient.user.username} on {self.appointment_time}"

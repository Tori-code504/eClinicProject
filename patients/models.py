from django.db import models
from django.conf import settings

class PatientProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'), 
        ('other', 'Other'),
    ])
    id_number = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255, blank= True, null=True)

    def __str__(self):
        return f"Patient Profile: {self.user.username}"

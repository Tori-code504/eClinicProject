from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
'''
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    phone_number = models.CharField(max_length=15,blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})" '''
'''    
class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient_profile')
    date_of_birth =models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'),('female', 'Female')])
    national_id = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Patient: {self.user.username}"
   ''' 
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doctor_appointments" )
    appointment_time = models.DateTimeField()
    service_time = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.patient.username} with Dr. {self.doctor.username} on {self.appointment_time}"

class QueueEntry(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete= models.CASCADE, related_name= 'queue_entry')
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



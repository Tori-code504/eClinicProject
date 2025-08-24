from django.contrib import admin
from .models import PatientProfile, Appointment, QueueEntry, MedicalRecord
from users.models import User

admin.site.register(User)
admin.site.register(PatientProfile)
admin.site.register(Appointment)
admin.site.register(QueueEntry)
admin.site.register(MedicalRecord)




from django.contrib import admin
from .models import User, PatientProfile, Appointment, QueueEntry, MedicalRecord

admin.site.register(User)
admin.site.register(PatientProfile)
admin.site.register(Appointment)
admin.site.register(QueueEntry)
admin.site.register(MedicalRecord)




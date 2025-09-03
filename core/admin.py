from django.contrib import admin
from .models import  Appointment, QueueEntry, MedicalRecord
from users.models import User

admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(QueueEntry)
admin.site.register(MedicalRecord)




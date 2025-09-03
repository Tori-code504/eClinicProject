from django.contrib import admin
from .models import QueueEntry, MedicalRecord

admin.site.register(QueueEntry)
admin.site.register(MedicalRecord)




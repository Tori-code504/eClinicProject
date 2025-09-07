from django.contrib import admin
from .models import QueueEntry


@admin.register(QueueEntry)
class QueueEntryAdmin(admin.ModelAdmin):
    list_display = ("appointment", "position", "created_at")


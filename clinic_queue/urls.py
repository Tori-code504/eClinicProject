from django.urls import path
from .views import QueueEntryDetailView, QueueEntryListCreateView

urlpatterns = [
    path("", QueueEntryListCreateView.as_view(), name="queue-list"),
    path("<int:pk>/", QueueEntryDetailView.as_view(), name="queue-detail"),
   
]

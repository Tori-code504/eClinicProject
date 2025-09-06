from django.urls import path
from . import views

urlpatterns = [
    path("", views.QueueListView.as_view(), name="queue-list"),
]

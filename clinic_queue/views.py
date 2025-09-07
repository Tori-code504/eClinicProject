from rest_framework import generics, permissions
from .models import QueueEntry
from .serializers import QueueEntrySerializer
from core.permissions import IsAdminOrNurseOrReadOnly


class BaseQueueEntryView:
    """Shared queryset logic for QueueEntry views."""

    def get_queryset(self):
        user = self.request.user
        if user.role in ["Admin", "Nurse"]:
            return QueueEntry.objects.all()
        # Patients see only their own queue entries
        return QueueEntry.objects.filter(appointment__patient__user=user)


class QueueEntryListCreateView(BaseQueueEntryView, generics.ListCreateAPIView):
    queryset = QueueEntry.objects.all()
    serializer_class = QueueEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrNurseOrReadOnly]

    def perform_create(self, serializer):
        """Extra safeguard: only Admin/Nurse can create entries."""
        if self.request.user.role not in ["Admin", "Nurse"]:
            raise permissions.PermissionDenied("Only Admins or Nurses can create queue entries.")
        serializer.save()


class QueueEntryDetailView(BaseQueueEntryView, generics.RetrieveUpdateDestroyAPIView):
    queryset = QueueEntry.objects.all()
    serializer_class = QueueEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrNurseOrReadOnly]

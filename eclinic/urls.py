from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenRefreshView # type: ignore
from users.views import CustomTokenObtainPairView


def api_root(request):
    return JsonResponse({
        "users": "/api/users/",
        "patients": "/api/patients/",
        "appointments": "/api/appointments/",
        "queue": "/api/queue/",
        "records": "/api/records/",
    })


urlpatterns = [
    path('admin/', admin.site.urls),

    # API root
    path("api/", api_root, name="api-root"),

    # User management
    path("api/users/", include("users.urls")),

    # JWT endpoints
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Other apps (fixed prefixes to avoid double "queue/queue/")
    path("api/patients/", include("patients.urls")),
    path("api/appointments/", include("appointments.urls")),
    path("api/queue/", include("clinic_queue.urls")),
    path("api/records/", include("records.urls")),
]

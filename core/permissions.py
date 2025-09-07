from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Allow only Admin users."""
    message = "Only Admin users are allowed."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == "Admin"


class IsPatient(permissions.BasePermission):
    """Allow only Patient users."""
    message = "Only Patient users are allowed."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == "Patient"


class IsPatientOrAdmin(permissions.BasePermission):
    """Allow Patients to manage their own objects, Admins can manage all."""
    message = "Only Admins or the owning Patient can access this."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == "Admin":
            return True
        # Safe check for `patient.user`
        patient = getattr(obj, "patient", None)
        return patient and patient.user == request.user


class IsDoctorOrAdminOrReadOnly(permissions.BasePermission):
    """Doctors and Admins can edit, others read-only."""
    message = "Only Doctors and Admins can modify. Others have read-only access."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role in ["Doctor", "Admin"]


class IsAdminOrNurseOrReadOnly(permissions.BasePermission):
    """Admins & Nurses can manage queue. Patients only view their own entries."""
    message = "Only Admins and Nurses can manage the queue. Patients may only view their own entries."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role in ["Admin", "Nurse"]:
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.role in ["Admin", "Nurse"]:
            return True
        # Patient can only see their own appointment queue entry
        return obj.appointment.patient.user == request.user


class IsAdminOrOwner(permissions.BasePermission):
    """Admins can access all, Patients only their own profile."""
    message = "Only Admins or the profile owner can access this."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Only Admins can list all profiles (works for both ViewSets and generics)
        if getattr(view, "action", None) == "list" and request.user.role != "Admin":
            return False

        return True

    def has_object_permission(self, request, view, obj):
        # Admin can do everything
        if request.user.role == "Admin":
            return True

        # Patients can only view/update their own profile
        if obj.user == request.user:
            if request.method in permissions.SAFE_METHODS or request.method in ["PUT", "PATCH"]:
                return True
            if request.method == "DELETE":
                return False  # Prevent patients from deleting their profile

        return False


class IsDoctorOrAdminOrOwner(permissions.BasePermission):
    """Doctors/Admins can create & edit records. Patients can only view their own records."""
    message = "Only Doctors and Admins can create or edit records. Patients may only view their own records."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role in ["Doctor", "Admin"]:
            return True
        if request.user.role == "Patient" and request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role in ["Doctor", "Admin"]:
            return True
        # Patients can only view their own records
        if request.user.role == "Patient" and obj.patient.user == request.user:
            return request.method in permissions.SAFE_METHODS
        return False

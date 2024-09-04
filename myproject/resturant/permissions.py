from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admin users to add a restaurant.
    """

    def has_permission(self, request, view):
        # Check if the request method is POST (i.e., create operation)
        if request.method == 'POST':
            # Check if the user is authenticated and is an admin
            return request.user and request.user.is_authenticated and request.user.is_admin
        return True
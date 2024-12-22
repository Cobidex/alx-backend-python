from rest_framework.permissions import BasePermission

class IsParticipant(BasePermission):
    """
    Custom permission to check if the user is a participant in the conversation.
    """
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()

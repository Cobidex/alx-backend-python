from rest_framework.permissions import BasePermission, IsAuthenticated

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to check if the user is a participant in the conversation.
    """
    def has_permission(self, request, view):
        """
        Allow only authenticated users to access the API.
        """
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Allow only participants to view, send, update, or delete messages.
        """
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        elif hasattr(obj, 'conversation_id'):
            return request.user in obj.conversation_id.participants.all()
        return False

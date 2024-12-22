from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipant

class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipant]

    def get_queryset(self):
        """
        Return conversations where the user is a participant.
        """
        return Conversation.objects.filter(participants=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Ensure the user is added as a participant when creating a conversation.
        """
        data = request.data
        data['participants'] = [request.user.id] + data.get('participants', [])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        """
        Return messages in conversations the user is part of.
        """
        return Message.objects.filter(conversation_id__participants=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Ensure the user is part of the conversation they are sending a message to.
        """
        conversation_id = request.data.get('conversation_id')
        if not Conversation.objects.filter(id=conversation_id, participants=request.user).exists():
            raise PermissionDenied("You are not a participant in this conversation.")
        return super().create(request, *args, **kwargs)
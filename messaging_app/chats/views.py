from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = []

    def get_queryset(self):
        """
        Return conversations where the user is a participant.
        """
        return Conversation.objects.filter(participants=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Create a new conversation with participants.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        conversation = serializer.save()
        return Response(
            {"message": "Conversation created successfully!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )

class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and creating messages within conversations.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

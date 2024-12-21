from django.shortcuts import get_object_or_404
from rest_framework import viewsets
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

class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and creating messages within conversations.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

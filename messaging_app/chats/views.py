from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, retrieving, and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        """
        Override create method to handle adding participants to a new conversation.
        """
        participants = request.data.get('participants', [])
        if len(participants) < 2:
            return Response({"error": "A conversation must have at least two participants."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Ensure all participants exist
        users = User.objects.filter(user_id__in=participants)
        if len(users) != len(participants):
            return Response({"error": "Some participants do not exist."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        conversation = Conversation.objects.create()
        conversation.participants.set(users)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, retrieving, and creating messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        """
        Override create method to send a message in an existing conversation.
        """
        conversation_id = request.data.get('conversation_id')
        sender_id = request.data.get('sender')
        message_body = request.data.get('message_body')

        # Validate conversation
        try:
            conversation = Conversation.objects.get(conversation_id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation does not exist."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # Validate sender
        try:
            sender = User.objects.get(user_id=sender_id)
        except User.DoesNotExist:
            return Response({"error": "Sender does not exist."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # Ensure sender is a participant in the conversation
        if not conversation.participants.filter(user_id=sender_id).exists():
            return Response({"error": "Sender is not a participant in this conversation."}, 
                            status=status.HTTP_403_FORBIDDEN)

        # Create and save the message
        message = Message.objects.create(conversation=conversation, sender=sender, message_body=message_body)
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

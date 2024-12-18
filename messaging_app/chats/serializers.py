from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'role', 'full_name']

    def get_full_name(self, obj):
        """
        Combines first and last name into a single full_name field.
        """
        return f"{obj.first_name} {obj.last_name}"


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.
    """
    sender_name = serializers.CharField(source='sender.first_name', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_name', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for Conversation model, including nested messages.
    """
    messages = MessageSerializer(many=True, read_only=True)
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']
        depth = 1

    def validate_participants(self, value):
        """
        Ensures a conversation includes at least two participants.
        """
        if len(value) < 2:
            raise serializers.ValidationError("A conversation must include at least two participants.")
        return value

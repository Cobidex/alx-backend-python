from django.db import models

class UnreadMessagesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(read=False).only('message_id', 'sender', 'receiver', 'content', 'timestamp', 'parent_message')
from django.db import models

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self):
        return super().get_queryset().filter(read=False).only('message_id', 'sender', 'receiver', 'content', 'timestamp', 'parent_message')
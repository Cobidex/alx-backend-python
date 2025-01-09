from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory, User

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                MessageHistory.objects.create(
                    message=old_message,
                    old_content=old_message.content
                )
                instance.edited = True
                instance.edited_by = instance.sender
                instance.edited_at = instance.timestamp
        except Message.DoesNotExist:
            pass

@receiver(post_delete, sender=User)
def clean_up_related_data(sender, instance, **kwargs):
    # Delete messages where the user is the sender or recipient
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(recipient=instance).delete()

    Notification.objects.filter(user=instance).delete()

    MessageHistory.objects.filter(user=instance).delete()

    print(f"Cleaned up related data for user: {instance.username}")
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

class MessagingTestCase(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='password')
        self.receiver = User.objects.create_user(username='receiver', password='password')

    def test_notification_creation(self):
        message = Message.objects.create(sender=self.sender, receiver=self.receiver, content="Hello!")
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.user, self.receiver)
        self.assertEqual(notification.message, message)

class MessagingTestCase(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='password')
        self.receiver = User.objects.create_user(username='receiver', password='password')
        self.message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Original Message"
        )

    def test_message_edit_logging(self):
        # Edit the message
        self.message.content = "Edited Message"
        self.message.save()

        # Check if history is logged
        self.assertEqual(MessageHistory.objects.count(), 1)
        history = MessageHistory.objects.first()
        self.assertEqual(history.old_content, "Original Message")
        self.assertTrue(self.message.edited)
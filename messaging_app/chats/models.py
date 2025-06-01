from django.db import models
from django.contrib.auth.models import AbstractUser
from time import timezone
# Create your models here.


class User(AbstractUser):
    pass


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation between {[user.username for user in self.participants.all()]}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, related_name="messages_sent", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"

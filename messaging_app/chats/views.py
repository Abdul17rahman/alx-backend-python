from django.shortcuts import render
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import MessageSerializer, ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('sent_at')
    serializer_class = MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

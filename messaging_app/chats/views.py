from django.shortcuts import render
from rest_framework import viewsets, filters, status, permissions
from .models import Conversation, Message
from .serializers import MessageSerializer, ConversationSerializer
from .permissions import IsParticipantOfConversation


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at']
    search_fields = ['participants_first_email']

    permission_classes = [permissions.IsAuthenticated,
                          IsParticipantOfConversation]


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body', 'sent_at']

    permission_classes = [permissions.IsAuthenticated]

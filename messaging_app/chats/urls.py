from rest_framework import routers
from django.urls import path, include
from chats import views


router = routers.DefaultRouter()

router.register(r"messages", views.MessageViewSet)
router.register(r"Conversations", views.ConversationViewSet)


path("", include(router.urls)),

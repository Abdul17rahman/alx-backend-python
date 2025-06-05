from rest_framework import routers
from django.urls import path, include
from chats import views


router = routers.DefaultRouter()

router.register(r"messages", views.MessageViewSet,
                basename='conversation-messages')
router.register(r"Conversations", views.ConversationViewSet,
                basename='conversation')


urlpatterns = [
    path("", include(router.urls)),
]

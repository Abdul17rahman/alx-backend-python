from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user in obj.participants.all()

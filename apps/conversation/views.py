from apps.conversation.serializers import ConversationSerializer
from apps.core.views import BaseCreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ConversationViewset(GenericViewSet, BaseCreateModelMixin):
    serializer_class = ConversationSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
from django.urls import path, include
from apps.conversation.settings import CONVERSATION_ENDPOINT
from rest_framework.routers import DefaultRouter
from apps.conversation.views import ConversationViewset

router = DefaultRouter()
router.register(CONVERSATION_ENDPOINT, ConversationViewset, basename='conversation')

urlpatterns = [
    path('', include(router.urls)),
]

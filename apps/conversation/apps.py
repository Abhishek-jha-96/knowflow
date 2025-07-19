from django.apps import AppConfig

from apps.conversation.settings import CONVERSATION_APP


class ConversationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = CONVERSATION_APP

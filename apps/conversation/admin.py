from django.contrib import admin

from apps.conversation.models import Conversation

# Register your models here.
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("question", "answer", "user")
    list_filter = ("user",)

admin.site.register(Conversation, ConversationAdmin)
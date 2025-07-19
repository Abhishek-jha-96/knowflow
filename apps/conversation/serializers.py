from apps.conversation.models import Conversation
from apps.conversation.tasks import get_answer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status


class ConversationSerializer(serializers.Serializer):
    """
    serializer to create conversations
    """
    
    question = serializers.CharField(write_only=True)
    answer = serializers.CharField(read_only=True)
    sources = serializers.CharField(read_only=True)
    

    def create(self, validated_data):
        request = self.context.get('request')

        instance = Conversation.objects.create(
            question=validated_data['question'],
            user=request.user
        )

        answer, collection_name = get_answer(instance)

        instance.answer = answer
        instance.save(update_fields=["answer"])

        return {
            "question": instance.question,
            "answer": instance.answer,
            "sources": collection_name
        }
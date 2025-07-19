from django.db import models

from apps.core.models import Timestamps
from apps.user.models import User

# Create your models here.
class Conversation(Timestamps):
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


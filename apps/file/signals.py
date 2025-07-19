from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.file.models import File
from apps.file.tasks import process_file_for_rag

@receiver(post_save, sender=File)
def on_file_uploaded(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: process_file_for_rag.delay(instance.id))


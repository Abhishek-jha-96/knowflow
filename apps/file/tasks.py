import time
import os
from celery import shared_task
from apps.core.rag_helper import RAGProcessor
from apps.file.utils import sanitize_collection_name
from apps.file.models import File
from pymupdf import FileDataError

@shared_task(bind=True, autoretry_for=(FileDataError, OSError), retry_kwargs={"max_retries": 3, "countdown": 2})
def process_file_for_rag(self, file_id):
    try:
        file = File.objects.get(id=file_id)
        file_path = file.file.path

        # Wait in case file isn't flushed to disk yet.
        retries = 0
        while not os.path.exists(file_path) and retries < 5:
            time.sleep(2)
            retries += 1

        rag = RAGProcessor()
        collection_name = sanitize_collection_name(file.title)
        rag.process_file(file_path, collection_name=collection_name)
        print(f"[✓] File {file.title} processed successfully.")

    except Exception as e:
        print(f"[✗] Failed to process file ID {file_id}: {str(e)}")
        raise e

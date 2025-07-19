import logging

from apps.conversation.task_helper import query_llm
from apps.core.rag_helper import RAGProcessor
from apps.file.models import File
from apps.file.utils import sanitize_collection_name


logger = logging.getLogger(__name__)


def get_answer(conv_instance):
    question = conv_instance.question

    # Get all file names and sanitize them
    collection_names = [
        sanitize_collection_name(title)
        for title in File.objects.values_list("title", flat=True)
    ]

    rag = RAGProcessor()
    prompt_tuple = rag.generate_prompt_from_question(
        question=question,
        collection_names=collection_names,
        n_results_per_collection=10,
    )
    answer = query_llm(prompt_tuple[0])
    return answer, prompt_tuple[1]


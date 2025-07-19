
# KnowFlow

**LLM-Powered Knowledge Assistant API using Django & ChromaDB**

## Description

KnowFlow is a Django REST API that enables document-based question answering using RAG (Retrieval-Augmented Generation). It extracts, chunks, embeds, and stores content from uploaded files, then queries this knowledge to answer user questions.

---

## Prerequisites

* [Docker](https://docs.docker.com/get-docker/)
* `docker-compose`:

  ```bash
  pip install docker-compose
  ```

---

## Pre-commit Setup

Run once:

```bash
pip install pre-commit
pre-commit install
```

Run before commit:

```bash
pre-commit run --all-files
```

---

## Running Locally

1. Copy `.envs/` to `.envs/local`
2. Generate RSA keys for JWT
3. Build Docker images:

   ```bash
   docker-compose build
   ```
4. Run services:

   ```bash
   docker-compose up -d
   ```
5. App: [http://localhost:8000](http://localhost:8000)
6. Access swagger at: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)
6. Stop services:

   ```bash
   docker-compose down
   ```

---

## Running Tests with Pytest

1. Build test image:

   ```bash
   docker-compose build
   ```
2. Run tests:

   ```bash
   docker-compose -f docker-compose.test.yml up -d
   ```

---

## Models Overview

### `File`

Stores uploaded documents.

```python
class File(models.Model):
    title = models.CharField(max_length=...)
    file = models.FileField(...)
```

### `Conversation`

Stores user questions and generated answers.

```python
class Conversation(models.Model):
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

---

## RAG Processing Flow (via `RAGProcessor`)

```text
1. User uploads a file (PDF/DOCX/TXT)
2. File content is extracted → chunked (using LangChain)
3. Chunks are embedded using SentenceTransformer
4. Embeddings + chunks are stored in ChromaDB under a collection (named after file title)
```

---

## Question Answering Flow

```text
1. User submits a question
2. The question is embedded → searched in all ChromaDB collections
3. Top results (by similarity) are ranked
4. The best chunk is selected → inserted into a prompt template
5. Prompt is sent to LLM to generate a final answer
```

---

## Technologies Used

* **Django REST Framework** (API)
* **Celery** (Async file processing)
* **ChromaDB** (Vector store)
* **SentenceTransformers** (Embedding)
* **LangChain** (Chunking)
* **Docker** (Dev environment)

---

from typing import List, Tuple, Optional
import os
import fitz  # PyMuPDF
import docx
import chromadb
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate

from knowflow.configurations.env_helpers import get_env_var, get_int_env_var


class RAGProcessor:
    def __init__(self, llm=None):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=64
        )

        self.chroma_client = chromadb.HttpClient(
            host=get_env_var("CHROMA_HOST"),
            port=get_int_env_var("CHROMA_PORT")
        )

        self.llm = llm  # Optional LLM for ranking

    def read_file(self, file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".pdf":
            return self._read_pdf(file_path)
        elif ext == ".docx":
            return self._read_docx(file_path)
        elif ext == ".txt":
            return self._read_txt(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    def _read_pdf(self, path: str) -> str:
        doc = fitz.open(path)
        return "\n".join([page.get_text() for page in doc])

    def _read_docx(self, path: str) -> str:
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])

    def _read_txt(self, path: str) -> str:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def chunk_file(self, text: str) -> List[str]:
        return self.splitter.split_text(text)

    def embed_chunks(self, chunks: List[str]) -> List[List[float]]:
        if not chunks:
            return []
        return self.model.encode(chunks, convert_to_tensor=False).tolist()

    def store_embeddings(
        self,
        collection_name: str,
        chunks: List[str],
        embeddings: List[List[float]],
    ):
        if not chunks or not embeddings:
            print(f"⚠️ No chunks or embeddings to store for {collection_name}.")
            return

        collection = self.chroma_client.get_or_create_collection(collection_name)
        metadatas = [{"chunk_index": i} for i in range(len(chunks))]
        ids = [f"{collection_name}_{i}" for i in range(len(chunks))]

        collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

    def process_file(self, file_path: str, collection_name: str):
        print(f"📄 Processing file: {file_path}")
        text = self.read_file(file_path)

        chunks = self.chunk_file(text)
        print(f"✂️  Total chunks: {len(chunks)}")

        embeddings = self.embed_chunks(chunks)
        print(f"🧠 Generated embeddings for {len(embeddings)} chunks.")

        self.store_embeddings(collection_name, chunks, embeddings)

        collection = self.chroma_client.get_or_create_collection(collection_name)
        print(f"✅ Stored {collection.count()} chunks in ChromaDB collection: {collection_name}")

    def generate_prompt_from_question(
        self,
        question: str,
        collection_names: List[str],
        n_results_per_collection: int = 3,
    ) -> Tuple[str, str]:
        """
        Searches across multiple ChromaDB collections and selects the single best context chunk
        from all results. Generates a prompt using that context.
        Returns:
            A tuple of (formatted_prompt, source_collection_name)
        """
        embedded_question = self.embed_chunks([question])[0]
        all_results = []
        
        # Collect all results from all collections
        for name in collection_names:
            collection = self.chroma_client.get_or_create_collection(name)
            result = collection.query(
                query_embeddings=[embedded_question],
                n_results=n_results_per_collection
            )
            
            docs = result.get("documents", [[]])[0]
            distances = result.get("distances", [[]])[0] if "distances" in result else [0.0] * len(docs)
            
            for doc, dist in zip(docs, distances):
                if doc and doc.strip():  # Only include non-empty documents
                    all_results.append((doc, dist, name))
        
        # Out of context
        if not all_results:
            no_context_template = (
                "You are an intelligent assistant. Answer the question based on your knowledge.\n\n"
                "Question: {question}\n"
                "Answer:"
            )
            prompt = PromptTemplate.from_template(no_context_template)
            return prompt.format(question=question.strip()), ""
        
        all_results.sort(key=lambda x: x[1])
        best_context, best_distance, best_collection = all_results[0]
        
        # Use the original template with the best context
        context_str = best_context.strip()
        template_str = (
            "You are an intelligent assistant. Use the provided context to answer the question as accurately and concisely as possible.\n\n"
            "If the answer is not directly present in the context, infer sensibly or say you don't know.\n"
            "Do not hallucinate or assume facts beyond the given information.\n\n"
            "Context:\n{context}\n\n"
            "Question: {question}\n"
            "Answer:"
        )
        
        prompt = PromptTemplate.from_template(template_str)
        return prompt.format(context=context_str, question=question.strip()), best_collection

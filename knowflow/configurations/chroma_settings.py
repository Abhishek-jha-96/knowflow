import chromadb
from knowflow.configurations.env_helpers import get_env_var, get_int_env_var


chroma_client = chromadb.HttpClient(
    host=get_env_var("CHROMA_HOST", "chroma"),
    port=get_int_env_var("CHROMA_PORT", "8001")
)

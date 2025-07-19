# Model contants
from knowflow.configurations.env_helpers import get_env_var


CONVERSATION_APP = "apps.conversation"

CONVERSATION_ENDPOINT = "ask-question"

# Token
HF_LLM_TOKEN = get_env_var("HUGGINGFACEHUB_API_TOKEN")
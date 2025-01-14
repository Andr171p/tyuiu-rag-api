from langchain_community.chat_models.gigachat import GigaChat

from src.config import settings
print(f"LLM {settings.giga_chat.name}")


class GigaChatLLM(GigaChat):
    model_config = {
        "credentials": settings.giga_chat.auth_key,
        "model_name": settings.giga_chat.name,
        "verify_ssl_certs": False,
        "profanity_check": False
    }

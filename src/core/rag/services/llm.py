from langchain_community.chat_models.gigachat import GigaChat

from src.config import settings


class GigaChatLLM(GigaChat):
    def __init__(
            self,
            credentials: str = settings.giga_chat.auth_key,
            scope: str = settings.giga_chat.scope,
            model_name: str = settings.giga_chat.name,
            verify_ssl_certs: bool = False,
            profanity_check: bool = False
    ) -> None:
        super().__init__(
            credentials=credentials,
            scope=scope,
            model=model_name,
            verify_ssl_certs=verify_ssl_certs,
            profanity_check=profanity_check
        )

from src.api_v1.container import chat_service
from src.services import ChatService


def get_chat_service() -> ChatService:
    return chat_service

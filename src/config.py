import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class EmbeddingsSettings(BaseSettings):
    # model_name: str = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    # name: str = "d0rj/e5-base-en-ru"
    name: str = "ai-forever/sbert_large_nlu_ru"
    model_kwargs: Dict[str, str] = {"device": "cpu"}
    encode_kwargs: Dict[str, bool] = {'normalize_embeddings': False}


class ChromaSettings(BaseSettings):
    host: str = "localhost"
    port: int = 8000


class ElasticSearchSettings(BaseSettings):
    host: str = os.getenv("ES_HOST")
    port: int = os.getenv("ES_PORT")
    password: str = os.getenv("ES_PASSWORD")
    username: str = os.getenv("ES_USERNAME")

    url: str = f"http://{username}:{password}@{host}:{port}"
    index_name: str = "tyuiu-index"


class PineconeSettings(BaseSettings):
    api_key: str = os.getenv("PINECONE_API_KEY")
    index_name: str = "tyuiu-index"


class GigaChatSettings(BaseSettings):
    client_id: str = os.getenv("CLIENT_ID")
    client_secret: str = os.getenv("CLIENT_SECRET")
    auth_key: str = os.getenv("AUTH_KEY")
    scope: str = os.getenv("GIGACHAT_API_PERS")
    url: str = os.getenv("AUTH_URL")
    name: str = os.getenv("MODEL_NAME")


class StaticSettings(BaseSettings):
    text_path: Path = BASE_DIR / "static" / "texts" / "ТИУ для абитуриентов.txt"
    prompt_path: Path = BASE_DIR / "static" / "prompt" / "Сотрудник приёмной комиссии.txt"


class APISettings(BaseSettings):
    name: str = "RAG GigaChat API"
    prefix: str = "/api/v1"


class Settings(BaseSettings):
    api_v1: APISettings = APISettings()
    embeddings: EmbeddingsSettings = EmbeddingsSettings()
    chroma: ChromaSettings = ChromaSettings()
    es: ElasticSearchSettings = ElasticSearchSettings()
    pc: PineconeSettings = PineconeSettings()
    giga_chat: GigaChatSettings = GigaChatSettings()
    static: StaticSettings = StaticSettings()


settings = Settings()

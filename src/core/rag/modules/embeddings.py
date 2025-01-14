from langchain.embeddings import HuggingFaceEmbeddings

from src.config import settings


class EmbeddingsModel(HuggingFaceEmbeddings):
    def __init__(
            self,
            model_name: str = settings.embeddings.name,
            model_kwargs: dict = settings.embeddings.model_kwargs,
            encode_kwargs: dict = settings.embeddings.encode_kwargs
    ) -> None:
        super().__init__(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )

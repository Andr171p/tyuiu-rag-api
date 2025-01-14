from langchain.embeddings import HuggingFaceEmbeddings

from src.config import settings
print(f"embed {settings.embeddings.model_name}")

class EmbeddingsModel(HuggingFaceEmbeddings):
    '''model_config = {
        "model_name": settings.embeddings.model_name,
        "model_kwargs": settings.embeddings.model_kwargs,
        "encode_kwargs": settings.embeddings.encode_kwargs
    }'''

    def __init__(
            self,
            model_name: str = settings.embeddings.model_name,
            model_kwargs: dict = settings.embeddings.model_kwargs,
            encode_kwargs: dict = settings.embeddings.encode_kwargs
    ) -> None:
        super().__init__(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )

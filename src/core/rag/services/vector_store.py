from typing import TYPE_CHECKING, Any

from chromadb import HttpClient
from chromadb.config import Settings
from langchain_community.vectorstores import Chroma

if TYPE_CHECKING:
    from langchain_core.embeddings import Embeddings


class ChromaVectorStore(Chroma):
    def __init__(
            self,
            embeddings: "Embeddings",
            client: Any = HttpClient(),
            settings: Settings = Settings(),
            collection_name: str = "tyuiu"
    ) -> None:
        super().__init__(
            client=client,
            client_settings=settings,
            embedding_function=embeddings,
            collection_name=collection_name
        )

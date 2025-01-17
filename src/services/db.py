from typing import (
    TYPE_CHECKING,
    List
)

from src.core.rag.services import ChromaVectorStore, EmbeddingsModel

if TYPE_CHECKING:
    from langchain_core.documents import Document


class DBService:
    vector_store = ChromaVectorStore(EmbeddingsModel())

    @classmethod
    def add_documents(cls, documents: List["Document"]) -> None:
        cls.vector_store.add_documents(documents)

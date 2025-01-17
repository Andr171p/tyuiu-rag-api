from typing import (
    TYPE_CHECKING,
    List
)

from src.core.rag.services import ElasticSearchRetriever

if TYPE_CHECKING:
    from langchain_core.documents import Document


class IndexService:
    retriever = ElasticSearchRetriever()

    @classmethod
    def add_documents(cls, documents: List["Document"]) -> None:
        cls.retriever.add_texts([
            document.page_content
            for document in documents
        ])

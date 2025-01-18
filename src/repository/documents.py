from typing import TYPE_CHECKING, List
from uuid import uuid4

if TYPE_CHECKING:
    from langchain_core.vectorstores import VectorStore
    from langchain_core.documents import Document


class DocumentsRepository:
    def __init__(self, vector_store: "VectorStore") -> None:
        self._vector_store = vector_store

    async def add_documents(
            self,
            documents: List["Document"]
    ) -> None:
        uuids = [str(uuid4()) for _ in range(len(documents))]
        await self._vector_store.aadd_documents(
            documents=documents,
            ids=uuids
        )

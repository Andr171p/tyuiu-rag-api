from typing import (
    TYPE_CHECKING,
    List
)

from src.core.rag.services import TextSplitter
from src.misc.loaders import load_txt
from src.config import settings

if TYPE_CHECKING:
    from pathlib import Path
    from langchain_core.documents import Document


class DocsService:
    splitter = TextSplitter()

    @classmethod
    def create_documents(
            cls,
            txt_path: Path = settings.static.text_path
    ) -> List[Document]:
        text = load_txt(txt_path)
        documents = cls.splitter.create_documents([text])
        return documents

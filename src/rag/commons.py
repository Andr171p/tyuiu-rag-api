from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from langchain_core.documents import Document


def parse_docs_content(docs: List["Document"]) -> str:
    return "\n\n".join([doc.page_content for doc in docs])

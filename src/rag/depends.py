from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.runnables.base import Runnable

from src.rag.container import (
    retriever,
    prompt,
    model,
    output_parser
)

from src.rag.factory import ChainFactory
from src.rag.commons import parse_docs_content


def get_chain() -> "Runnable":
    factory = ChainFactory(
        retriever=retriever,
        prompt=prompt,
        model=model,
        output_parser=output_parser
    )
    chain = factory.create_chain(parse_docs_content)
    return chain

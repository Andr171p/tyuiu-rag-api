from typing import (
    TYPE_CHECKING,
    Optional
)

from langchain.retrievers import EnsembleRetriever
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.core.rag.services import (
    ElasticSearchRetriever,
    ChromaVectorStore,
    EmbeddingsModel,
    GigaChatLLM
)
from src.core.rag.utils import format_docs
from src.misc.loaders import load_txt
from src.config import settings

if TYPE_CHECKING:
    from langchain_core.retrievers import BaseRetriever
    from langchain_core.prompts.chat import BaseChatPromptTemplate
    from langchain_core.language_models.chat_models import BaseChatModel
    from langchain_core.output_parsers.transform import BaseTransformOutputParser
    from langchain_core.runnables.base import Runnable


class ChainBuilder:
    __slots__ = ("_ensemble_retriever", "_chat_prompt", "_llm", "_output_parser")

    def __init__(self) -> None:
        self._ensemble_retriever: Optional["BaseRetriever"] = None
        self._chat_prompt: Optional["BaseChatPromptTemplate"] = None
        self._llm: Optional["BaseChatModel"] = None
        self._output_parser: Optional["BaseTransformOutputParser"] = None

    def set_ensemble_retriever(
            self,
            k: int = 3,
    ) -> "ChainBuilder":
        elastic_search_retriever = ElasticSearchRetriever()
        chroma = ChromaVectorStore(EmbeddingsModel())
        chroma.delete_collection()
        chroma_retriever = chroma.as_retriever(search_kwargs={"k": k})
        self._ensemble_retriever = EnsembleRetriever(
            retrievers=[
                elastic_search_retriever,
                chroma_retriever
            ],
            weights=[0.4, 0.6]
        )
        return self

    def set_chat_prompt(self) -> "ChainBuilder":
        template: str = load_txt(settings.static.prompt_path)
        self._chat_prompt = ChatPromptTemplate.from_template(template)
        return self

    def set_llm(self) -> "ChainBuilder":
        self._llm = GigaChatLLM()
        return self

    def set_output_parser(self) -> "ChainBuilder":
        self._output_parser = StrOutputParser()
        return self

    def create_chain(self) -> "Runnable":
        chain = (
            {"context": self._ensemble_retriever | format_docs, "input": RunnablePassthrough()} |
            self._chat_prompt |
            self._llm |
            self._output_parser
        )
        return chain

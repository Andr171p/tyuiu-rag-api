from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_core.runnables.base import Runnable

from src.rag import get_chain


class ChatService:
    def __init__(self, chain: "Runnable" = get_chain()) -> None:
        self._chain = chain

    async def answer_on_question(self, question: str) -> str:
        return await self._chain.ainvoke(question)

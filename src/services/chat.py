from src.core.rag.chain import ChainBuilder


class ChatService:
    def __init__(self) -> None:
        self._chain = (
            ChainBuilder()
            .set_ensemble_retriever()
            .set_chat_prompt()
            .set_llm()
            .set_output_parser()
        ).create_chain()

    async def answer_on_question(self, question: str) -> str:
        return await self._chain.ainvoke(question)

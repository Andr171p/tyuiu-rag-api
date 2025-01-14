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
        return await self._chain.ainvoke({"text": question})


'''from elasticsearch import Elasticsearch
from src.config import settings

# Подключение к Elasticsearch
es = Elasticsearch(settings.es.url)

# Имя индекса, который нужно удалить
index_name = settings.es.index_name

# Удаление индекса
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)
    print(f"Индекс '{index_name}' успешно удалён.")
else:
    print(f"Индекс '{index_name}' не существует.")'''


chat_service = ChatService()

import asyncio
async def main() -> None:
    answer = await chat_service.answer_on_question("Расскажи о ТИУ")
    print(answer)


asyncio.run(main())

from fastapi import (
    APIRouter,
    Depends,
    Query,
    status
)
from fastapi.responses import JSONResponse

from src.services import ChatService
from src.api_v1.depends import get_chat_service
from src.schemas import AnswerResponse
from src.config import settings


rag_router = APIRouter(
    prefix=f"{settings.api_v1.prefix}/chat",
    tags=["RAG GigaChat"]
)


@rag_router.get(path="/answer/", response_model=AnswerResponse)
async def get_answer_on_question(
        query: str = Query(...),
        chat_service: ChatService = Depends(get_chat_service)
) -> JSONResponse:
    answer: str = await chat_service.answer_on_question(query)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "answer": answer
            }
        }
    )

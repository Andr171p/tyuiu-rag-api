from contextlib import (
    asynccontextmanager,
    AbstractAsyncContextManager
)

from fastapi import FastAPI

from src.services import DocsService, DBService, IndexService


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    documents = DocsService.create_documents()
    DBService.add_documents(documents)
    IndexService.add_documents(documents)
    yield

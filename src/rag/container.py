from langchain.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models.gigachat import GigaChat
from langchain_core.output_parsers.string import StrOutputParser

from langchain.text_splitter import RecursiveCharacterTextSplitter

from pinecone import Pinecone, ServerlessSpec

from src.misc.loaders import load_txt
from src.config import settings


embeddings = HuggingFaceEmbeddings(
    model_name=settings.embeddings.name,
    model_kwargs=settings.embeddings.model_kwargs,
    encode_kwargs=settings.embeddings.encode_kwargs
)

vector_store = PineconeVectorStore(
    index=Pinecone(settings.pc.api_key).Index(settings.pc.index_name),
    embedding=embeddings
)

retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 1, "score_threshold": 0.5},
)

prompt = ChatPromptTemplate.from_template(load_txt(settings.static.prompt_path))

model = GigaChat(
    credentials=settings.giga_chat.auth_key,
    scope=settings.giga_chat.scope,
    model=settings.giga_chat.name,
    verify_ssl_certs=False,
    profanity_check=False
)

output_parser = StrOutputParser()

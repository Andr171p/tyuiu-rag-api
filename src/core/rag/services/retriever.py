from elasticsearch import Elasticsearch
from langchain.retrievers import ElasticSearchBM25Retriever

from src.config import settings


class ElasticSearchRetriever(ElasticSearchBM25Retriever):
    def __init__(
            self,
            client: Elasticsearch = Elasticsearch(settings.es.url),
            index_name: str = settings.es.index_name,
            k: int = 3
    ) -> None:
        super().__init__(
            client=client,
            index_name=index_name,
            k=k
        )

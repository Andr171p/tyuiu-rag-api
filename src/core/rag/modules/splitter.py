from typing import Callable

from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextSplitter(RecursiveCharacterTextSplitter):
    def __init__(
            self,
            chunk_size: int = 1500,
            chunk_overlap: int = 500,
            length_function: Callable = len
    ) -> None:
        super().__init__(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=length_function
        )

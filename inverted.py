from typing import List


class Index:
    def __init__(self):
        pass

    def index(self, id_: int, text: str) -> None:
        """
        Index a document
        id_ - id of the document
        text - text of the document
        """
        pass

    def all_words(self, *words: str) -> List[int]:
        """
        Return a list of document ids that contain all given words
        """
        return []

    def any_words(self, *words: str) -> List[int]:
        """
        Return a list of document ids that contain any of the specified words
        """
        return []
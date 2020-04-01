
from abc import ABC, abstractmethod


class FileHashAlgorithm(ABC):

    @abstractmethod
    def hash_file(self, file: str) -> str:
        pass


from abc import ABC, abstractmethod
from logging import Logger
from .file_hash_algorithm import FileHashAlgorithm


class Action(ABC):

    def __init__(self, logger: Logger, file_hash_algorithm: FileHashAlgorithm):
        self.logger = logger
        self.file_hash_algorithm = file_hash_algorithm

    def execute(self, file: str) -> None:
        hash: str = self.file_hash_algorithm.hash_file(file)
        self.logger.debug('file: %s hash: %s' % (file, hash))
        if self._hash_check(hash):
            self._hash_found_action(hash, file)
        else:
            self._store_hash(hash, file)

    def show_stats(self) -> None:
        self.logger.error('Statistics not implemented.')

    @abstractmethod
    def _hash_check(self, hash: str) -> bool:
        pass

    @abstractmethod
    def _store_hash(self, hash: str, file: str) -> None:
        pass

    @abstractmethod
    def _hash_found_action(self, hash: str, file: str) -> None:
        pass

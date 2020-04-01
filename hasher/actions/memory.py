
from os import stat as os_stat
from ..action import Action
from ..file_hash_algorithm import FileHashAlgorithm
from logging import Logger


class Memory(Action):

    def __init__(self, logger: Logger, file_hash_algorithm: FileHashAlgorithm):
        super().__init__(logger, file_hash_algorithm)
        self.store = {}
        self.stats = {'count': 0, 'size': 0}

    def _hash_check(self, hash: str) -> bool:
        if hash in self.store.keys():
            return True
        else:
            return False

    def _store_hash(self, hash: str, file: str) -> None:
        self.store[hash] = file

    def _hash_found_action(self, hash: str, file: str) -> None:
        self.logger.info('DUPLICATE FOUND! File: %s (copies: %s)' % (file, self.store[hash]))
        self._stats_count(file)

    def _stats_count(self, file: str) -> None:
        self.stats['count'] += 1
        self.stats['size'] += os_stat(file).st_size

    def show_stats(self) -> None:
        size = self._convert_bytes(self.stats['size'])
        self.logger.info('count: %s, size: %s' % (self.stats['count'], size))

    @staticmethod
    def _convert_bytes(num: int) -> str:
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0


from file_hasher.file_hash_algorithm import FileHashAlgorithm
import hashlib


class Md5(FileHashAlgorithm):

    def hash_file(self, file: str) -> str:
        hash_md5 = hashlib.md5()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


import pytest
from file_hash_algorithms.md5 import Md5


@pytest.fixture()
def md5():
    return Md5()


def test_hash(fs, md5):
    fs.create_file('test.file')
    assert md5.hash_file('test.file') == 'd41d8cd98f00b204e9800998ecf8427e'


def test_hash_file_with_contents(fs, md5):
    fs.create_file('test.file', contents='foobarfoobar')
    assert md5.hash_file('test.file') == '59faa421729e846dd800dce59943bfc0'


def test_hash_of_not_existing_file(fs, md5):
    with pytest.raises(FileNotFoundError):
        md5.hash_file('test.file')

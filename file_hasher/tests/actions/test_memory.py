
import pytest
from ...actions.memory import Memory
from unittest import mock


@pytest.fixture
def prepared_fs(fs):
    fs.create_file('test1.txt')
    fs.create_file('test2.txt')
    return prepared_fs


@pytest.fixture
def hash_algorithm():
    values = {'test1.txt': 'foo', 'test2.txt': 'bar'}

    def return_value(key: str) -> str:
        return values[key]

    obj = mock.Mock()
    obj.hash_file.side_effect = return_value
    return obj


@pytest.fixture
def memory(hash_algorithm):
    return Memory(
        mock.Mock(),
        hash_algorithm
    )


def test_memory(prepared_fs, memory):
    memory.execute('test1.txt')
    assert memory.stats['count'] == 0


def test_memory_two(prepared_fs, memory):
    memory.execute('test1.txt')
    memory.execute('test2.txt')
    assert memory.stats['count'] == 0


def test_memory_doubled(prepared_fs, memory):
    memory.execute('test1.txt')
    memory.execute('test1.txt')
    assert memory.stats['count'] == 1


from unittest import mock
import pytest
from dir_scanner import DirScanner


@pytest.fixture
def prepared_fs(fs):
    fs.create_file('test.foo')
    fs.create_file('test.bar')
    fs.create_file('sub/foo.bar')
    return fs


@pytest.fixture
def action():
    return mock.Mock()


@pytest.fixture
def dir_scanner(action):
    return DirScanner(
        mock.Mock(),
        '/',
        action
    )


def test_scann(prepared_fs, dir_scanner, action):
    dir_scanner.run()
    action.execute.assert_has_calls(
        [
            mock.call('//test.foo'),
            mock.call('//test.bar'),
        ],
        any_order=True
    )


def test_scann_recursive(prepared_fs, dir_scanner, action):
    dir_scanner.set_recursive()
    dir_scanner.run()
    action.execute.assert_has_calls(
        [
            mock.call('//test.foo'),
            mock.call('//test.bar'),
            mock.call('/sub/foo.bar'),
        ],
        any_order=True
    )


import argparse


class Arguments:
    directory: str = '.'
    recursive: bool = False
    loglevel: str = 'INFO'


def parse():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='2020 Łukasz Bacik <mail@luka.sh> https://github.com/lbacik/file-hasher'
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default=Arguments.directory,
        help='directory to scan'
    )
    parser.add_argument(
        '-r',
        '--recursive',
        action="store_true",
        default=Arguments.recursive,
        help='check directories recursively'
    )
    parser.add_argument(
        '--loglevel',
        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'],
        default=Arguments.loglevel,
        help=''
    )
    return parser.parse_args(namespace=Arguments)

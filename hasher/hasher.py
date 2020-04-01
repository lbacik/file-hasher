"""
Hasher is a module for searching identical files
"""

import logging
import parse_arguments
from actions.memory import Memory
from file_hash_algorithms.md5 import Md5
from dir_scanner import DirScanner

LOG_FORMAT = '%(asctime)-15s %(levelname)s %(message)s'


def main(args: parse_arguments.Arguments, logger: logging.Logger):
    logger.debug('Directory to scan: %s' % args.directory)

    scanner = instantiate_scanner(logger)

    if args.recursive:
        scanner.set_recursive()

    scanner.run(args.directory)
    scanner.show_stats()


def instantiate_scanner(logger: logging.Logger):
    hash_method = Md5()
    action = Memory(logger, hash_method)
    return DirScanner(logger, action)


if __name__ == "__main__":
    args = parse_arguments.parse()

    logging.basicConfig(format=LOG_FORMAT, level=args.loglevel)
    logger = logging.getLogger('hasher')

    main(args, logger)

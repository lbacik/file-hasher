
import os
from pathlib import Path
from .action import Action


class DirScanner():

    def __init__(self, logger, action: Action):
        self.logger = logger
        self.action = action
        self.recursive = False

    def set_recursive(self) -> None:
        self.recursive = True

    def run(self, directory: str) -> None:
        for root, dirs, files in os.walk(directory):
            self.logger.debug('root: %s' % (root,))
            self.logger.debug('dirs: %s' % (dirs.__str__(),))
            for file in files:
                if not Path('%s/%s' % (root, file)).is_symlink():
                    self.action.execute("%s/%s" % (root, file))
            if not self.recursive:
                break

    def show_stats(self):
        self.action.show_stats()

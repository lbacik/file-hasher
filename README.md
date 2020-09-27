# File Hasher

The tool for searching identical files

```bash
$ file-hasher -h
usage: hasher [-h] [-r]
              [--loglevel {CRITICAL,ERROR,WARNING,INFO,DEBUG,NOTSET}]
              [directory]

positional arguments:
  directory             directory to scan

optional arguments:
  -h, --help            show this help message and exit
  -r, --recursive       check directories recursively
  --loglevel {CRITICAL,ERROR,WARNING,INFO,DEBUG,NOTSET}

2020 Łukasz Bacik <mail@luka.sh> https://github.com/lbacik/hasher
```

## Installation

Python3 is required!

    pip install file-hasher

## Development

    pip install -r dev-requirements.txt

    pytest src/file_hasher/tests
    pylint src/file_hasher

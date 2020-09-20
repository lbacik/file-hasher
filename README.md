
Hasher - the tool for searching identical files

```bash
$ hasher -h
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

## development

    pip install -r dev-requirements.txt

    pytest file_hasher/tests
    pylint file_hasher
    
    
crate test venv:

    python3 -m venv venv-test
    source venv-test/bin/activate

build and install package locally:
    
    pip install -r dev-requirements.txt
    pytest src/file_hasher/tests
    python setup.py sdist bdist_wheel
    pip install . 

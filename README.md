# Test for local pypi

## Usage for testing
build `demo_package`, collect it into package storage, run pypi
```
make run
```

## Custom usage
First of all: Create dir `.packages` in project root path
Then:
```bash
make run_clean
```

## How to install from local pypi
```bash
pip3 install -i http://localhost:8080/simple demo_package  # or any your package
```

## TODO
1. Setup pypi for pushing packages

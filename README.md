# mappi

![Tests](https://github.com/bmwant/mappi/actions/workflows/tests.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/mappi)](https://pypi.org/project/mappi/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mappi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![EditorConfig](https://img.shields.io/badge/-EditorConfig-grey?logo=editorconfig)](https://editorconfig.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

### Usage

```bash
$ pip install mappi

# generate sample config file
$ mappi config > mappi.yml

# adjust routes as needed or create your own config
$ vim mappi.yml

# start your webserver
$ mappi
```

### Development

```bash
$ poetry install
$ poetry run python -m mappi

$ poetry run mappi


$ pre-commit install
$ pre-commit autoupdate
```

# mappi

![Tests](https://github.com/bmwant/mappi/actions/workflows/tests.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/mappi)](https://pypi.org/project/mappi/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mappi)


[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![EditorConfig](https://img.shields.io/badge/-EditorConfig-grey?logo=editorconfig)](https://editorconfig.org/)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)


<p align="center">
  <img alt="Logo" src="https://github.com/bmwant/mappi/blob/main/assets/logo.png">
</p>

### Installation

```bash
$ pip install mappi
$ mappi  # run server with example configuration
```

### Usage

```bash
# generate minimal config file
$ mappi config > mappi.yml

# adjust routes as needed or create your own config
$ vim mappi.yml

# dump configuration with all the options available to a file
$ mappi config --full > mappi.yml

# start your webserver
$ mappi

# start server with configuration stored in different filename
$ mappi --config my-config-file.yml
```

### Contributing

See [DEVELOP.md](https://github.com/bmwant/mappi/blob/main/DEVELOP.md) for the development setup and contributing guide.

### Development

* Clone repository (should be your own fork for contributing)
```bash
$ git clone git@github.com:bmwant/mappi.git
```

* Install dependencies
```bash
$ poetry install
```

* Run application
```bash
$ poetry run mappi
# or
$ poetry run python -m mappi
```

* Run unittests
```bash
$ make tests
```

* Run integration tests
```bash
$ make integration-tests
```

* Install pre-commit hooks
```bash
$ pre-commit install
$ pre-commit autoupdate  # update versions of existing hooks
```

.PHONY: build
build:
	@rm -rf dist/
	@rm -rf build/
	@poetry build

.PHONY: tests
tests:
	@poetry run pytest -sv tests

.PHONY: coverage
coverage:
	@poetry run pytest --cov=mappi tests

.PHONY: coverage-report
coverage-report:
	@poetry run pytest --cov=mappi --cov-report=html tests

.PHONY: isort
isort:
	@poetry run isort .

.PHONY: black
black:
	@poetry run black .

.PHONY: lint
lint:
	@poetry run flake8 .

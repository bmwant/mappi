FROM python:3.11-slim

ENV HOME="/root"
WORKDIR $HOME

RUN apt-get update && apt-get install -y --no-install-recommends \
  curl \
  make

ARG POETRY_VERSION=1.3.2
RUN curl -sSL https://install.python-poetry.org | python3 - --version ${POETRY_VERSION}

ENV PATH="${HOME}/.local/bin:${PATH}"

COPY pyproject.toml poetry.lock README.md ./
COPY mappi/ ./mappi/
RUN poetry install

EXPOSE 5858
ENTRYPOINT ["poetry", "run"]
CMD ["mappi"]

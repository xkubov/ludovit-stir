FROM python:3.10

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -y install \
		rustc && \
	rm -rf /var/lib/apt/lists/*

# Install pinned poetry version.
RUN pip install --no-cache-dir 'poetry==1.3.1'

# Copying this first will improve caching and re-runs.
COPY poetry.lock pyproject.toml /app/

WORKDIR /app

# Project initialization:
# Disable using virtualenvs. Docker is already isolated environment.
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

COPY . /app

RUN poetry install

ENTRYPOINT ["ludovit_stir"]

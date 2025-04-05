FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ENV POETRY_VERSION=1.8.4
# RUN curl -sSL https://install.python-poetry.org | python3 -
# ENV PATH="/root/.local/bin:$PATH"

RUN pip3 install poetry==1.8.4
ENV POETRY_VIRTUALENVS_CREATE=false
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-interaction --no-ansi
COPY . /app
EXPOSE 8000

CMD ["poetry", "run", "python", "run.py"]
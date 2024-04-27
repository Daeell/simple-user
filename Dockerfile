FROM python:3.11-slim

# .pyc 파일을 생성하지 않도록 설정합니다.
ENV PYTHONDONTWRITEBYTECODE 1
# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하도록 설정합니다.
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN pip install poetry

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-dev

# Run your app
COPY . .
EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]
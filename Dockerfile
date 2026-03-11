FROM python:3.12
WORKDIR /app
RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
COPY src ./src
RUN uv pip install --system .
COPY . .
CMD ["python", "hello.py"]
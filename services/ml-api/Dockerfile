FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

RUN uv sync --frozen

# Copy the rest of the application
COPY . .

# Run with uvicorn for development
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8100", "--reload"]
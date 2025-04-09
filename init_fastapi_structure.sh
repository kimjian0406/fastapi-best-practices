#!/bin/bash

PROJECT_ROOT="."

mkdir -p $PROJECT_ROOT/app/api
mkdir -p $PROJECT_ROOT/app/core
mkdir -p $PROJECT_ROOT/app/models
mkdir -p $PROJECT_ROOT/app/schemas
mkdir -p $PROJECT_ROOT/app/services
mkdir -p $PROJECT_ROOT/tests

cat <<EOL > $PROJECT_ROOT/app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}
EOL

cat <<EOL > $PROJECT_ROOT/pyproject.toml
[tool.black]
line-length = 88

[tool.isort]
profile = "black"

[tool.mypy]
strict = true

[tool.ruff]
line-length = 88
select = ["E", "F", "I"]
EOL

cat <<EOL > $PROJECT_ROOT/.pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff

  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.12.0
    hooks:
      - id: isort
EOL

cat <<EOL > $PROJECT_ROOT/requirements.txt
fastapi
uvicorn
pydantic
EOL

echo "✅ FastAPI 프로젝트 기본 구조 생성 완료!"


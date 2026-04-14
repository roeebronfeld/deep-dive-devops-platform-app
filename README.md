# deep-dive-devops-platform-app

Minimal first backend scaffold for a future DevOps platform app.

## What is included

- FastAPI backend in `backend/app/main.py`
- `GET /health` endpoint
- `GET /pods` endpoint returning mock Kubernetes-like data
- Dockerfile based on `python:3.11-slim`
- Non-root container user
- `docker-compose.yml` with backend and a placeholder PostgreSQL service

## Run locally with Docker Compose

```bash
docker compose up --build
```

The backend will be available at `http://localhost:8000`.

## Endpoints

- `GET /health`
- `GET /pods`

## Notes

- PostgreSQL is included only as a future placeholder service.
- The backend does not connect to PostgreSQL yet.
- There is no Kubernetes integration yet.
- There is no CI/CD setup yet.

<<<<<<< HEAD
# deep-dive-devops-platform-app

Minimal first backend and frontend scaffold for a future DevOps platform app.

## What is included

- FastAPI backend in `backend/app/main.py`
- Minimal frontend in `frontend/`
- `GET /health` endpoint
- `GET /pods` endpoint returning mock Kubernetes-like data
- Dockerfile based on `python:3.11-slim`
- Non-root container user
- `docker-compose.yml` with frontend, backend, and a placeholder PostgreSQL service

## Run locally with Docker Compose

```bash
docker compose up --build
```

The frontend will be available at `http://localhost:3000`.
The backend will be available at `http://localhost:8000`.

## Endpoints

- `GET /health`
- `GET /pods`

## Frontend

- The frontend page fetches `http://localhost:8000/health`
- The frontend page fetches `http://localhost:8000/pods`
- It renders a simple health summary and a basic list of pods

## Notes

- PostgreSQL is included only as a future placeholder service.
- The backend does not connect to PostgreSQL yet.
- The frontend calls the backend directly from the browser for local development.
- There is no Kubernetes integration yet.
- There is no CI/CD setup yet.
=======
# deep-dive-devops-platform-app
>>>>>>> origin/main

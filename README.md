# deep-dive-devops-platform-app

Minimal early-stage scaffold for a DevOps platform app.

## What is included

- FastAPI backend in `backend/`
- Minimal frontend in `frontend/`
- `docker-compose.yml` for local development
- GitHub Actions CI in `.github/workflows/ci.yml`
- Placeholder PostgreSQL service for future work

## Local run

```bash
docker compose up --build
```

- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`

## Current behavior

- `GET /health` returns a simple backend health response
- `GET /pods` returns mock Kubernetes-like pod data
- The frontend displays the health response and pod data
- The frontend reaches the backend through the frontend container proxy

## Notes

- PostgreSQL is included but is not used by the backend yet
- There is no real database integration yet
- There is no Kubernetes integration yet
- CI is intentionally minimal and only validates basic syntax, Compose config, and Docker builds

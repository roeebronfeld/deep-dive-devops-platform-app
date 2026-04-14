# deep-dive-devops-platform-app

Minimal early-stage scaffold for a DevOps platform app.

## What is included

- FastAPI backend in `backend/`
- Minimal frontend in `frontend/`
- `docker-compose.yml` for local development
- Minimal Kubernetes manifests in `k8s/` for the backend and frontend
- GitHub Actions CI in `.github/workflows/ci.yml`
- Placeholder PostgreSQL service for future work

## Local run with Docker Compose

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

## Kubernetes

Build and load the images for your local cluster, then apply the manifests:

```bash
docker build -t deep-dive-devops-platform-app-backend:latest ./backend
docker build -t deep-dive-devops-platform-app-frontend:latest ./frontend
minikube image load deep-dive-devops-platform-app-backend:latest
minikube image load deep-dive-devops-platform-app-frontend:latest
kubectl apply -f k8s/
```

Check the pods and services:

```bash
kubectl get pods
kubectl get services
```

Port-forward the frontend service:

```bash
kubectl port-forward service/frontend 8080:80
```

Then open `http://localhost:8080`.

## Notes

- PostgreSQL is included in Docker Compose but is not used by the backend yet
- Kubernetes currently includes only the backend and frontend
- There is no real database integration yet
- There is no Kubernetes ingress yet
- CI is intentionally minimal and only validates basic syntax, Compose config, and Docker builds

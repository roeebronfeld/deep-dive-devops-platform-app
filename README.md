# deep-dive-devops-platform-app

Minimal early-stage scaffold for a DevOps platform app.

## What is included

- FastAPI backend in `backend/`
- Minimal frontend in `frontend/`
- `docker-compose.yml` for local development
- Minimal Kubernetes manifests in `k8s/` for the backend and frontend
- Minimal Helm chart in `helm/deep-dive-devops-platform/`
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

## Helm

Render the chart locally:

```bash
helm template deep-dive-devops-platform ./helm/deep-dive-devops-platform
```

Install or upgrade it on your local cluster:

Use the same locally built and loaded images from the Kubernetes section above, then run:

```bash
helm upgrade --install deep-dive-devops-platform ./helm/deep-dive-devops-platform
```

Check the resources:

```bash
kubectl get deployments
kubectl get services
```

Port-forward the frontend and verify the app:

```bash
kubectl port-forward service/frontend 8080:80
curl http://localhost:8080/health
```

You can also open `http://localhost:8080`.

## Ingress

Enable the Minikube nginx ingress addon:

```bash
minikube addons enable ingress
```

Install or upgrade the chart with ingress enabled:

```bash
helm upgrade --install deep-dive-devops-platform ./helm/deep-dive-devops-platform \
  --set ingress.enabled=true
```

Check the ingress resource:

```bash
kubectl get ingress
```

Test it locally with the Minikube IP and the configured host:

```bash
curl http://$(minikube ip) -H "Host: deep-dive.local"
```

If you want to open it in a browser, add `deep-dive.local` to your hosts file pointing to the Minikube IP.

## Notes

- PostgreSQL is included in Docker Compose but is not used by the backend yet
- Kubernetes currently includes only the backend and frontend
- There is no real database integration yet
- Kubernetes ingress is optional and disabled by default in the Helm chart
- CI is intentionally minimal and only validates basic syntax, Compose config, and Docker builds

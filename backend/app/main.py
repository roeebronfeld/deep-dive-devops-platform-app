from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Deep Dive DevOps Platform Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "backend",
    }


@app.get("/pods")
def pods() -> dict:
    return {
        "deployment": {
            "name": "demo-api",
            "namespace": "dev",
            "desiredReplicas": 2,
            "readyReplicas": 2,
        },
        "pods": [
            {
                "name": "demo-api-abc123",
                "phase": "Running",
                "ready": True,
                "restartCount": 0,
                "nodeName": "node-a",
                "ageSeconds": 300,
            },
            {
                "name": "demo-api-def456",
                "phase": "Running",
                "ready": True,
                "restartCount": 1,
                "nodeName": "node-b",
                "ageSeconds": 280,
            },
        ],
    }

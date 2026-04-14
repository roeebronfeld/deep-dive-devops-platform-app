from fastapi import FastAPI


app = FastAPI(title="Deep Dive DevOps Platform Backend")


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

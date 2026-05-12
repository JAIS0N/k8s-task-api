# 🚀 Learnings: Docker + Kubernetes + FastAPI

## 🧠 Docker Fundamentals

- Docker is a **containerization platform** used to package applications with dependencies.
- An **Image** is a blueprint (code + runtime + dependencies).
- A **Container** is a running instance of an image.

### Key Concepts
- `Dockerfile` defines how to build the image
- `docker build` → creates image
- `docker run` → runs container

### Port Mapping

```
HOST_PORT : CONTAINER_PORT
```

Example:

```
8081:8080
```

- 8081 → accessed from browser
- 8080 → inside container (app server)

---

## 🧩 Docker Compose

- Used to run **multiple containers together**
- Defines:
  - services
  - ports
  - networking

### Example

```
services:
  go-gin:
  node-express:
  python-fastapi:
```

### Key Learning

- Each container has its **own isolated port space**
- Multiple services can run on **same internal port (8080)**

---

## 🌐 Container Networking

### External (Host → Container)

```
localhost:8081 → container:8080
```

### Internal (Container → Container)

```
http://service-name:port
```

Example:

```
http://node-express:8080
```

---

## ☸️ Kubernetes Fundamentals

Kubernetes manages containers at scale.

### Core Components

| Concept    | Meaning                         |
|------------|---------------------------------|
| Pod        | Smallest unit (runs container)  |
| Deployment | Manages pods (replicas, restart)|
| Service    | Exposes application             |
| Cluster    | Group of machines               |

---

## 🔁 Docker vs Kubernetes

| Docker           | Kubernetes           |
|------------------|----------------------|
| Runs containers  | Manages containers   |
| Single machine   | Cluster (multi-node) |
| Manual scaling   | Auto scaling         |

---

## ⚙️ Kubernetes Deployment

### Deployment

- Defines number of replicas
- Manages pod lifecycle

### Service

- Exposes pods
- Provides stable endpoint

Example:

```
NodePort → exposes app externally
```

---

## 🔥 FastAPI Learnings

### API Design

- `GET /tasks` → fetch tasks
- `POST /tasks` → create task
- `GET /health` → health check

### Pydantic

- Validates request body
- Ensures type safety

### Concurrency

- Used `Lock` to prevent race conditions

---

## ⚠️ Stateless Design

- Each pod has its own memory
- In-memory list is NOT shared

```
Pod 1 → ["task1"]
Pod 2 → []
```

👉 Need DB for shared state

---

## 🧪 Debugging Learnings

### 1. Kubernetes not running

```
kubectl get nodes
```

Fix:
- Enable Kubernetes in Docker Desktop

---

### 2. ErrImageNeverPull

Cause:
- Kubernetes cannot find local image

Fix:

```
docker build -t k8s-task-api:latest ./app
```

---

### 3. ContainerCreating stuck

- Wait for image pull / startup
- Check logs:

```
kubectl describe pod <pod-name>
```

---

### 4. NodePort not accessible

Fix:

```
kubectl port-forward service/task-api-service 8088:80
```

---

### 5. PowerShell JSON issues

Fix:

```
Invoke-RestMethod -Method Post -Uri "http://localhost:8088/tasks" -Body '{"task":"value"}'
```

---

## 🧠 Key Concepts Mastered

- Containerization (Docker)
- Multi-service orchestration (Compose)
- Kubernetes deployments
- Pod lifecycle
- Service exposure
- Debugging real cluster issues
- API design and validation
- Concurrency basics

---

## 🎯 Final Takeaway

- Docker → package and run apps
- Kubernetes → manage and scale apps
- FastAPI → build APIs
- Debugging → critical real-world skill

---

## 🚀 Next Improvements

- Add database (PostgreSQL / Redis)
- Add autoscaling (HPA)
- Add monitoring (Prometheus + Grafana)
- Deploy to cloud (AWS / GCP / Azure)

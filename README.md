# Local Kubernetes Deployment Demo

A containerized Python application orchestrated locally using Kubernetes, showcasing high availability, automated self-healing, and internal load balancing.

## Overview
This project demonstrates foundational container orchestration concepts using a local Kubernetes cluster (Docker Desktop). It moves beyond single-container deployments to manage a multi-pod application ecosystem, focusing on reliability, scaling, and network abstraction.

## Architecture & Components

The project consists of four core files:
1. **`app.py`**: A lightweight, long-running Python HTTP web server acting as a mock API health check.
2. **`Dockerfile`**: Packages the app into a secure container image, exposing port `8080` and enforcing non-root execution (`USER 10001`).
3. **`deployment.yaml`**: A Kubernetes Deployment manifest that:
   - Maintains **2 replicas** (identical pods running side-by-side) for high availability.
   - Enforces `imagePullPolicy: Always` to ensure local image updates are cleanly synchronized.
   - Provides automated **self-healing** (instantly replacing crashed or terminated pods).
4. **`service.yaml`**: A Kubernetes NodePort Service that:
   - Acts as a dynamic **internal load balancer**, distributing incoming requests across active pods using label selectors (`app: python-app`).
   - Abstracts away ephemeral pod IP addresses behind a stable networking layer.

## How to Run Locally

1. **Enable Kubernetes** in your Docker Desktop settings.
2. **Build the container image**:
   ```bash
   docker build --no-cache -t my-python-app:v2 .
3. **Deploy to the cluster**:
    ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
4. **Verify running pods**:
    ```bash
   kubectl get pods
5. **Test the load-balanced service (via port-forwarding)**:
    ```bash
   kubectl port-forward service/python-app-service 8080:80
5. **Test the load-balanced service (via port-forwarding)**:
    ```bash
   kubectl port-forward service/python-app-service 8080:80
6. **Then open a separate terminal and test the endpoint:**:
    ```bash
   curl http://localhost:8080
# Autoscale Web Application using Kubernetes HPA

A project demonstrating how to deploy a containerized Flask web application on a Kubernetes cluster and enable automatic pod scaling using the Horizontal Pod Autoscaler (HPA). A load generator is included to simulate traffic and observe autoscaling behavior in action.

---

## Overview

| Component | Technology |
|---|---|
| Web Framework | Flask (Python) |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Scaling Strategy | Horizontal Pod Autoscaler (CPU-based) |
| Monitoring | Kubernetes Metrics Server |

---

## Architecture

The system is composed of the following layers:

1. **Flask Application** — A lightweight web server that responds to incoming HTTP requests.
2. **Docker Image** — The Flask app is packaged into a container image for portability and consistency.
3. **Kubernetes Deployment** — Manages multiple replicas of the containerized application.
4. **Service** — Exposes the application within the cluster or externally via a stable endpoint.
5. **Metrics Server** — Collects real-time CPU and memory metrics from running pods.
6. **Horizontal Pod Autoscaler (HPA)** — Monitors CPU utilization and adjusts the number of pod replicas accordingly.
7. **Load Generator** — Simulates concurrent HTTP traffic to trigger and observe scaling events.

---

## Prerequisites

Ensure the following are available before proceeding:

- A running Kubernetes cluster (Minikube, Kind, GKE, EKS, or AKS)
- `kubectl` CLI configured to access your cluster
- Metrics Server installed and running in the cluster
- Docker installed for building the container image

---

## Setup and Deployment

### 1. Build the Docker Image

```bash
docker build -t flask-hpa-app:latest .
```

If using Minikube, point your shell to the Minikube Docker daemon first:

```bash
eval $(minikube docker-env)
```

### 2. Deploy the Application

Apply the Kubernetes deployment and service manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 3. Verify the Deployment

```bash
kubectl get pods
kubectl get svc
```

### 4. Install the Metrics Server (if not already present)

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Verify it is running:

```bash
kubectl get deployment metrics-server -n kube-system
```

### 5. Create the Horizontal Pod Autoscaler

```bash
kubectl apply -f k8s/hpa.yaml
```

Or create it imperatively:

```bash
kubectl autoscale deployment flask-app \
  --cpu-percent=50 \
  --min=1 \
  --max=10
```

Check HPA status:

```bash
kubectl get hpa
```

### 6. Run the Load Generator

```bash
kubectl apply -f k8s/load-generator.yaml
```

This deploys a pod that continuously sends requests to the Flask service, driving up CPU usage and triggering the autoscaler.

---

## Observing Autoscaling

Watch the HPA and pod count in real time:

```bash
kubectl get hpa -w
kubectl get pods -w
```

As CPU utilization rises above the target threshold, Kubernetes will scale up the number of replicas. Once the load generator is stopped and usage drops, the HPA will scale back down after a cooldown period.

---

## Configuration Reference

### HPA Parameters

| Parameter | Description | Default |
|---|---|---|
| `minReplicas` | Minimum number of pods | 1 |
| `maxReplicas` | Maximum number of pods | 10 |
| `targetCPUUtilizationPercentage` | CPU threshold to trigger scaling | 50% |

### Resource Requests (deployment.yaml)

HPA requires resource requests to be defined on the container. Example:

```yaml
resources:
  requests:
    cpu: "100m"
  limits:
    cpu: "200m"
```

---

## Project Structure

```
.
├── app/
│   ├── app.py              # Flask application
│   └── requirements.txt    # Python dependencies
├── Dockerfile              # Container image definition
├── k8s/
│   ├── deployment.yaml     # Kubernetes Deployment
│   ├── service.yaml        # Kubernetes Service
│   ├── hpa.yaml            # Horizontal Pod Autoscaler
│   └── load-generator.yaml # Load generator pod
└── README.md
```

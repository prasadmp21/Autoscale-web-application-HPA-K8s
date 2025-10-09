# Autoscale Web Application using Kubernetes HPA

This project demonstrates how to deploy a containerized Flask web application on a Kubernetes cluster and enable **automatic scaling** of pods using the **Horizontal Pod Autoscaler (HPA)**. It also includes a load generator to simulate traffic and observe autoscaling behavior.

---

## 🚀 Overview

- **Technology Stack:** Flask (Python), Docker, Kubernetes  
- **Scaling:** Horizontal Pod Autoscaler (CPU-based)  
- **Monitoring:** Kubernetes Metrics Server  
- **Goal:** Automatically scale the number of pods based on CPU utilization

---

## 🧱 Architecture

1. **Flask App** — A simple web application responding to HTTP requests.  
2. **Docker Image** — The Flask app is containerized.  
3. **Kubernetes Deployment** — Runs multiple replicas of the web app.  
4. **Service** — Exposes the app within the cluster or externally.  
5. **Metrics Server** — Collects CPU/memory metrics for autoscaling.  
6. **Horizontal Pod Autoscaler (HPA)** — Adjusts pod replicas based on CPU usage.  
7. **Load Generator** — Simulates traffic to trigger scaling events.

---

## 🧰 Prerequisites

Before you begin, make sure you have the following:

- A running **Kubernetes cluster** (e.g., Minikube, Kind, GKE, EKS, AKS)
- **kubectl** CLI configured to access your cluster  
- **Metrics Server** installed in the cluster  
- **Docker** installed (for building the image)

---

## ⚙️ Setup and Deployment

### 1️⃣ Clone the repository

```bash
git clone https://github.com/prasadmp21/Autoscale-web-application-HPA-K8s.git
cd Autoscale-web-application-HPA-K8s

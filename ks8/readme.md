# Lets do it

## Setup

### 1. Install Homebrew

First, install Kind using Homebrew:

```bash
brew install kind helm localstack kubectl
```

### 2. Create a Kind Cluster

Create a Kind cluster:

```bash
kind create cluster --name localstack-cluster
```

### 3. Install LocalStack with Homebrew

Next, install LocalStack using Homebrew:

```bash
brew install localstack
```

Start LocalStack with the --network flag:

```bash
docker network create localstack-network
localstack start --network localstack-network
```

### 4. Configure Networking

Ensure LocalStack and Kind can communicate by connecting them to the same Docker network:

```bash
docker network connect localstack-network kind-control-plane
```

### 6. Create a Kubernetes Deployment YAML

Create a YAML file for your Kubernetes deployment that interacts with LocalStack. For example, create a file named `deployment.yaml`:

### 7. Deploy Services in Kind

Use kubectl to apply your Kubernetes deployment:

```bash
kubectl apply -f deployment.yaml
```

# Setting Up a Local K8s Cluster with Thanos and LLM Demo

## Outline

1. **Introduction**

   - Overview of the task
   - Objectives

2. **Setup and Installation**

   - Setting up Kind
   - Installing Helm
   - Deploying Thanos
   - Running the LLM demo with Ollama

3. **Generating Metrics and Familiarization**
   - Generating metrics
   - Exploring Helm charts
   - Core features of Kind, kubectl, and Helm

## Instructions and Commands

### Create a Local K8s Cluster with Kind

1. Install Kind: `curl -Lo ./kind https://kind.sigs.k8s.io/dl/linux/amd64 && chmod +x ./kind`
2. Create a cluster: `./kind create cluster --name thanos-cluster`
3. Check config: `kubectl config current-context`

### Install Helm and Deploy Thanos

1. Install Helm: `curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash`
2. Add the Thanos Helm repository: `helm repo add thanos https://charts.thanos.io/thanos`
3. Update the Helm repositories: `helm repo update`
4. Deploy Thanos using OCI registry: `helm install my-release oci://registry-1.docker.io/bitnamicharts/thanos`

### Access Thanos UIs

1. Visit the Thanos Query UI: `http://localhost:9090`
2. Visit the Thanos Compact UI: `http://localhost:9091`

### Verify Thanos Deployment

1. Check the Thanos pods: `kubectl get pods -l app=thanos`

## References
- https://charts.thanos.io/thanos
- https://github.com/bitnami/charts/tree/main/bitnami/thanos

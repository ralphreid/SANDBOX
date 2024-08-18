# Kubernetes Kustomize Setup

This project demonstrates the use of Kustomize to manage Kubernetes configurations.

## Install

To set up the cluster, run: `kind create cluster --name wicked-demo`

- Initialize Kustomize
  Run: `kustomize build`
- Apply Configuration
  Run: `kustomize apply`

## Managing Multiple Clusters

If you have multiple clusters, you can specify the context to ensure you are applying configurations to the correct cluster.

- List all contexts:

  ```sh
  kubectl config get-contexts
  ```

- Set the context to the desired cluster:

  ```sh
  kubectl config use-context <context-name>
  ```

Replace `<context-name>` with the name of the context you want to use.

### **Step 5: Deploy Prometheus to Your Cluster**

Now, you can deploy Prometheus to your Kubernetes cluster using `kubectl`.

#### 1. **Apply Development Configuration**

To apply the development configuration:

```sh
kubectl apply -k kustomize/overlays/dev
```

#### 2. **Apply Production Configuration**

To apply the production configuration:

```sh
kubectl apply -k kustomize/overlays/prod
```

## Operator Principles

### 1. Declarative Configuration
Kubernetes uses declarative configuration to manage the desired state of the cluster. Ensure your configurations are stored in version control.

### 2. Idempotency
Operations should be idempotent, meaning applying the same configuration multiple times should not change the state after the first application.

### 3. Observability
Implement logging, monitoring, and alerting to observe the state of your applications and infrastructure.

### 4. Automation
Automate repetitive tasks using CI/CD pipelines and Kubernetes operators.

## Exploring the Cluster and CLI Tools

### 1. kubectl
`kubectl` is the command-line tool for interacting with the Kubernetes API server.

- List all resources:
  ```sh
  kubectl get all
  ```

- Describe a resource:
  ```sh
  kubectl describe <resource> <name>
  ```

- View logs:
  ```sh
  kubectl logs <pod-name>
  ```

### 2. kubeadm
`kubeadm` is a tool for bootstrapping a Kubernetes cluster.

### 3. Helm
Helm is a package manager for Kubernetes, useful for managing complex applications.

## Ensuring Services are Running

### 1. Check Service Status
Ensure that all services are running and healthy.

- List all services:
  ```sh
  kubectl get services
  ```

- Check the status of a deployment:
  ```sh
  kubectl rollout status deployment/<deployment-name>
  ```

### 2. Health Checks
Implement readiness and liveness probes in your pod specifications to ensure the health of your applications.

## Migration from Docker-Compose to Kubernetes

### 1. Translate docker-compose.yml to Kubernetes
Use tools like `kompose` to convert `docker-compose.yml` files to Kubernetes resource files.

- Install kompose:
  ```sh
  sudo curl -L https://github.com/kubernetes/kompose/releases/download/v1.21.0/kompose-linux-amd64 -o /usr/local/bin/kompose
  sudo chmod +x /usr/local/bin/kompose
  ```

- Convert docker-compose.yml:
  ```sh
  kompose convert
  ```

### 2. Apply the Converted Files
Apply the converted Kubernetes resource files to your cluster.

- Apply resources:
  ```sh
  kubectl apply -f <resource-file>
  ```

## Using Workbench Tools

### 1. Visual Studio Code
Use the Kubernetes extension for VS Code to manage your cluster.

- Install the Kubernetes extension from the VS Code marketplace.

### 2. Lens
Lens is a powerful IDE for managing Kubernetes clusters.

- Download and install Lens from its official website.

### 3. K9s
K9s is a terminal-based UI to interact with your Kubernetes clusters.

- Install K9s:
  ```sh
  sudo snap install k9s
  ```

- Run K9s:
  ```sh
  k9s
  ```

## Deploy Prometheus to Your Cluster

### 1. Set the Context (Optional)
If you have multiple clusters, you can set the context to the desired cluster. The context represents a specific cluster and user combination. Here's an example of how a context might look like:

```sh
kubectl config use-context my-cluster-context
```

Replace `<context-name>` with the name of the context you want to use.

### 2. Apply Development Configuration
To apply the development configuration:

```sh
kubectl apply -k kustomize/overlays/dev
```

### 3. Apply Production Configuration
To apply the production configuration:

```sh
kubectl apply -k kustomize/overlays/prod
```

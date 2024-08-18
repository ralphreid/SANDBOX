# Kubernetes Kustomize Setup

This project demonstrates the use of Kustomize to manage Kubernetes configurations.

## Install

To set up the cluster, run: `kind create cluster --name my-fun-work`

- Initialize Kustomize
  Run: `kustomize build`
- Apply Configuration
  Run: `kustomize apply`

## Ref

- https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/

### Setting Up a Minimal Prometheus Service Using Kustomize

This guide will walk you through setting up a minimal Prometheus service on Kubernetes using Kustomize. We will create and structure the necessary files step-by-step, and include relevant `kubectl` commands to help you get familiar with the CLI and Kustomize.

### **Step 1: Install and Set Up Kustomize**

Before we begin, ensure that you have `kubectl` installed and configured to communicate with your Kubernetes cluster. Kustomize is now integrated into `kubectl`, so you don't need to install it separately.

- **Verify `kubectl` version**:
  ```sh
  kubectl version --client
  ```

- **Verify Kustomize support in `kubectl`**:
  ```sh
  kubectl kustomize --help
  ```

### **Step 2: Directory Structure**

We'll start by creating the directory structure for our Prometheus setup.

```sh
mkdir -p kustomize/base
mkdir -p kustomize/overlays/dev
mkdir -p kustomize/overlays/prod
```

This structure will contain:

- **Base**: The core configuration files for Prometheus.
- **Overlays**: Environment-specific customizations (for example, development and production environments).

### **Step 3: Create Base Configuration Files**

Now, we'll define the base configuration files that will be shared across all environments.

#### 1. **Prometheus Deployment (`kustomize/base/deployment.yaml`)**

Create the base deployment manifest for Prometheus.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      containers:
        - name: prometheus
          image: prom/prometheus:v2.37.0
          ports:
            - containerPort: 9090
```

#### 2. **Prometheus Service (`kustomize/base/service.yaml`)**

Create the service manifest for Prometheus.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: prometheus-service
spec:
  type: ClusterIP
  ports:
    - port: 9090
      targetPort: 9090
  selector:
    app: prometheus
```

#### 3. **ConfigMap for Prometheus Configuration (`kustomize/base/configmap.yaml`)**

Prometheus requires a configuration file. We'll use a ConfigMap to store this configuration.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
      - job_name: 'prometheus'
        static_configs:
          - targets: ['localhost:9090']
```

#### 4. **Base Kustomization File (`kustomize/base/kustomization.yaml`)**

This file will reference the resources defined above.

```yaml
resources:
  - ../../base

patchesStrategicMerge:
  - patch.yaml
  - ../../base

patchesStrategicMerge:
  - patch.yaml
  - deployment.yaml
  - service.yaml
  - configmap.yaml

configMapGenerator:
  - name: prometheus-config
    files:
      - prometheus.yml=prometheus.yml
  - deployment.yaml
  - service.yaml
  - configmap.yaml

configMapGenerator:
  - name: prometheus-config
    files:
      - prometheus.yml=prometheus.yml
```

### **Step 4: Create Environment-Specific Overlays**

Now, let's create overlays for development and production environments.

#### 1. **Development Overlay (`kustomize/overlays/dev/kustomization.yaml`)**

This overlay will use the base resources with minimal changes.

```yaml
resources:
  - ../../base

patchesStrategicMerge:
  - patch.yaml
```

**Patch for Development (`kustomize/overlays/dev/patch.yaml`):**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
spec:
  replicas: 1
  template:
    spec:
      containers:
        - name: prometheus
          image: prom/prometheus:v2.37.0
```

#### 2. **Production Overlay (`kustomize/overlays/prod/kustomization.yaml`)**

The production overlay might scale Prometheus differently or use a different image tag.

```yaml
resources:
  - ../../base

patchesStrategicMerge:
  - patch.yaml
```

**Patch for Production (`kustomize/overlays/prod/patch.yaml`):**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: prometheus
          image: prom/prometheus:v2.37.0
```

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

### **Step 6: Verify the Deployment**

After deploying, you can verify that the Prometheus service is running correctly.

#### 1. **Check Pods**

List the running pods to verify that Prometheus is deployed:

```sh
kubectl get pods
```

#### 2. **Check Services**

List the services to ensure that the Prometheus service is exposed:

```sh
kubectl get services
```

### **Step 7: Access Prometheus**

Prometheus should be accessible at the ClusterIP address of the service within the Kubernetes cluster. For testing, you can use port forwarding to access Prometheus locally.

```sh
kubectl port-forward svc/prometheus-service 9090:9090
```

Then, navigate to `http://localhost:9090` in your browser to access the Prometheus UI.

### **Summary**

- **Base Configuration**: Defines the core deployment and service for Prometheus, along with a ConfigMap for the Prometheus configuration.
- **Environment Overlays**: Allows customization for different environments, such as adjusting the number of replicas or using different image tags.
- **Resource Generators**: Used to dynamically generate ConfigMaps, making configuration management easier.

This setup is minimal yet effective for deploying Prometheus in different environments using Kustomize. It showcases how Kustomize simplifies managing Kubernetes resources across multiple environments with clear and maintainable configurations.

## Directory Structure

- `kustomize/base`: Contains the base configurations for ConfigMap, Deployment, and Service.
- `kustomize/overlays/dev`: Contains the overlay configurations for the development environment.
- `kustomize/overlays/prod`: Contains the overlay configurations for the production environment.

## Base Configurations

The base directory includes the following resources:

- `configmap.yaml`: Defines a ConfigMap with example properties.
- `deployment.yaml`: Defines a Deployment with 3 replicas of an Nginx container.
- `service.yaml`: Defines a Service to expose the Deployment.

## Overlays

### Development Overlay

The development overlay references the base configurations and applies development-specific patches.

### Production Overlay

The production overlay references the base configurations and applies production-specific patches.

## Usage

To apply the configurations using Kustomize, navigate to the desired overlay directory and run:

```sh
kubectl apply -k .
```

For example, to apply the development overlay:

```sh
cd kustomize/overlays/dev
kubectl apply -k .
```

To apply the production overlay:

```sh
cd kustomize/overlays/prod
kubectl apply -k .
```

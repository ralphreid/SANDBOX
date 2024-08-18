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

### **Step 5: Deploy Prometheus to Your Cluster**

Now, you can deploy Prometheus to your Kubernetes cluster using `kubectl`.

#### 1. **Set the Context (Optional)**

If you have multiple clusters, you can set the context to the desired cluster. The context represents a specific cluster and user combination. Here's an example of how a context might look like:

```sh
kubectl config use-context my-cluster-context
```

Replace `<context-name>` with the name of the context you want to use.

#### 2. **Apply Development Configuration**

To apply the development configuration:

```sh
kubectl apply -k kustomize/overlays/dev
```

#### 3. **Apply Production Configuration**

To apply the production configuration:

```sh
kubectl apply -k kustomize/overlays/prod
```

> > > > > > > REPLACE

</source>

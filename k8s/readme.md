# Lets do it

## Setup

### 1. Install Homebrew

First, install Kind using Homebrew:

```bash
brew install kind helm localstack kubectl terraform
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
export LOCALSTACK_AUTH_TOKEN=$(pbpaste)

docker network create localstack-network
localstack start --network localstack-network -d
```

### 4. Configure Networking

Ensure LocalStack and Kind can communicate by connecting them to the same Docker network:

```bash
docker network connect localstack-network localstack-cluster-control-plane
```

### 6. Create a Kubernetes Deployment YAML

Create a YAML file for your Kubernetes deployment that interacts with LocalStack. For example, create a file named `deployment.yaml`:

### 7. Deploy Services in Kind

Use kubectl to apply your Kubernetes deployment:

```bash
kubectl apply -f deployment.yaml

kubectl apply -f nginx-deployment.yaml
kubectl port-forward deployment/nginx-deployment 8080:80
```

Now, open your web browser and navigate to http://localhost:8080 to see the Nginx welcome page.

Check Pod Status: Ensure that the Nginx pod is running correctly.
`kubectl get pods`

Look for the status of the Nginx pod. It should be in the Running state.
Check Logs: Inspect the logs of the Nginx pod to see if there are any errors.
`kubectl logs <nginx-pod-name>`

### 8. Deploy with Terraform

Initialize Terraform: Navigate to the directory containing main.tf and initialize Terraform:

```bash
terraform init
```

Plan the Infrastructure: Create an execution plan to preview the changes that Terraform will make to your infrastructure:

```bash
terraform plan
```

Apply the Configuration: Apply the changes required to reach the desired state of the configuration:

````bash

### 8. Deploy with Terraform

Initialize Terraform: Navigate to the directory containing main.tf and initialize Terraform:

```bash
terraform init
````

Plan the Infrastructure: Create an execution plan to preview the changes that Terraform will make to your infrastructure:

```bash
terraform plan
```

Apply the Configuration: Apply the changes required to reach the desired state of the configuration:

```bash
terraform apply -auto-approve
```

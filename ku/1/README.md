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

```
 helm install my-release oci://registry-1.docker.io/bitnamicharts/thanos
Pulled: registry-1.docker.io/bitnamicharts/thanos:15.7.19
Digest: sha256:2818cec2d4162903b9ee2d3a6c69e0bb8da3f036b74dc9579ff00097f4eaaf33
NAME: my-release
LAST DEPLOYED: Sat Aug 10 21:30:44 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: thanos
CHART VERSION: 15.7.19
APP VERSION: 0.36.0

** Please be patient while the chart is being deployed **

Thanos chart was deployed enabling the following components:
- Thanos Query

Thanos Query can be accessed through following DNS name from within your cluster:

    my-release-thanos-query.default.svc.cluster.local (port 9090)

To access Thanos Query from outside the cluster execute the following commands:

1. Get the Thanos Query URL by running these commands:

    export SERVICE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].port}" services my-release-thanos-query)
    kubectl port-forward --namespace default svc/my-release-thanos-query ${SERVICE_PORT}:${SERVICE_PORT} &
    echo "http://127.0.0.1:${SERVICE_PORT}"

2. Open a browser and access Thanos Query using the obtained URL.

WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
  - query.resources
  - queryFrontend.resources
+info https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
```

### Access Thanos UIs

1. Visit the Thanos Query UI: `http://localhost:9090`

### Verify Thanos Deployment

To teardown the resources created by the Thanos deployment, follow these steps:

1. Delete the Thanos release: `helm uninstall my-release`
2. Delete the Kind cluster: `kind delete cluster --name thanos-cluster`

Remember to verify that all resources have been successfully deleted by running `kubectl get all` after executing these commands.

1. `kubectl get pods --all-namespaces -l app=thanos`
2. `kubectl get pods -n <namespace> -l app=thanos`
3. Check the Thanos pods: `kubectl get pods -l app=thanos`

Use Helmfile for managing multiple Helm charts and environments: Helmfile allows you to define and manage multiple Helm charts and their configurations in a single file.

:
Deploy with Helmfile:

file apply

## References

- https://charts.thanos.io/thanos
- https://github.com/bitnami/charts/tree/main/bitnami/thanos
- https://github.com/bitnami/charts/blob/main/bitnami/thanos/README.md
- https://github.com/bitnami/charts/tree/main/bitnami/kube-prometheus
- https://k8slens.dev
- https://kind.sigs.k8s.io/docs/user/quick-start/

## Setup

### Directory Structure

Create command:

```shell
mkdir -p charts/{clearml/templates,grafana/templates,opentelemetry/templates,my-app/templates} helmfile.d terraform/{dev,prod} values && \
touch charts/clearml/{Chart.yaml,values.yaml,values-dev.yaml,values-prod.yaml} charts/grafana/{Chart.yaml,values.yaml} charts/opentelemetry/{Chart.yaml,values.yaml} charts/my-app/{Chart.yaml,values.yaml,values-dev.yaml,values-prod.yaml} helmfile.d/{helmfile.yaml,dev.yaml,prod.yaml} terraform/dev/{main.tf,terraform.tfvars} terraform/prod/{main.tf,terraform.tfvars} values/{common.yaml,dev.yaml,prod.yaml}
```

```shell
├── charts/                                # Custom Helm charts
│   ├── clearml/                           # ClearML Helm chart
│   │   ├── templates/
│   │   ├── Chart.yaml
│   │   ├── values.yaml                    # Default values
│   │   ├── values-dev.yaml                # Dev environment-specific values
│   │   └── values-prod.yaml               # Prod environment-specific values
│   ├── grafana/                           # Grafana Helm chart
│   │   ├── templates/
│   │   ├── Chart.yaml
│   │   └── values.yaml
│   ├── opentelemetry/                     # OpenTelemetry Helm chart
│   │   ├── templates/
│   │   ├── Chart.yaml
│   │   └── values.yaml
│   └── my-app/                            # Example application Helm chart
│       ├── templates/
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── values-dev.yaml
│       └── values-prod.yaml
├── helmfile.d/                            # Helmfile configurations
│   ├── helmfile.yaml                      # Base Helmfile (all charts)
│   ├── dev.yaml                           # Helmfile config for development
│   └── prod.yaml                          # Helmfile config for production
├── terraform/                             # Terraform for AWS infrastructure
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── dev/                               # Dev-specific Terraform configuration
│   │   ├── main.tf
│   │   └── terraform.tfvars
│   └── prod/                              # Prod-specific Terraform configuration
│       ├── main.tf
│       └── terraform.tfvars
└── values/                                # Common values
    ├── common.yaml                        # Common values for all environments
    ├── dev.yaml                           # Dev environment values
    └── prod.yaml                          # Prod environment values
```

### Helm Chart Configuration

1. Create a new chart: `helm create my-chart`
2. Install the chart: `helm install my-chart ./my-chart`
3. Upgrade the chart: `helm upgrade my-chart ./my-chart`
4. Uninstall the chart: `helm uninstall my-chart`

### Helmfile Configuration

Helmfile helps manage deployments across multiple environments by layering environment-specific configurations on top of the base configurations.

### Terraform Configuration

Terraform should be used to provision the necessary AWS infrastructure, such as the EKS cluster, networking, IAM roles, etc. Separate configurations for development and production environments ensure isolation and appropriate resource allocation.

### Deploying with Helmfile

With this structure, you can deploy your application to different environments using Helmfile.

### Benefits of This Pattern

- Reusability: Common values are defined once and shared across environments, reducing duplication.
- Environment Isolation: Separate values files and Terraform configurations ensure environments are isolated and configured appropriately.
- Flexibility: Helmfile allows easy management of different environments with minimal duplication.
- Infrastructure as Code: Terraform handles infrastructure provisioning, ensuring consistency and repeatability.

### Leveraging Fargate and Cloud Map

- Fargate Support: If you’re deploying to Fargate, ensure your Helm chart is configured to use Fargate profiles in your EKS cluster by setting appropriate annotations in your deployment templates.
- Cloud Map for Service Discovery: Integrate AWS Cloud Map in your Helm templates by adding annotations to your services, ensuring they register with Cloud Map for service discovery:

```yaml
annotations:
  service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
  service.beta.kubernetes.io/aws-cloud-map-discovery: "enabled"
  service.beta.kubernetes.io/aws-cloud-map-namespace: "my-namespace"
```

## Key Commands and Tips

This guide provides a comprehensive workflow for developing, testing, and deploying ClearML on AWS EKS using Kind, Helmfile, Kustomize, and Terraform.

**Summary of Tips and Probes**

- **Kind:** `kubectl get nodes` to check the cluster status.
- **Helm:** `helm get values <release-name>` to inspect configurations.
- **Kustomize:** `kustomize build <directory> | less` to review the generated manifests.
- **Grafana:** Use `kubectl port-forward` to access UIs like Grafana.
- **ClearML:** `kubectl logs -l app=clearml-webserver` to troubleshoot issues.
- **EKS:** `aws eks describe-cluster` and `kubectl get nodes` to verify EKS cluster health.

### Initial Setup with Kind

To set up the required clusters, follow these steps:

```bash
kind create cluster --name wicked-demo
```

- Use `kind create cluster` to create a Kubernetes cluster with Kind.
- Specify the cluster name with the `--name` flag, e.g., "wicked-demo".
- Kind runs Kubernetes clusters inside Docker containers, ideal for local development and testing.
- Retrieve the kubeconfig file with `kind get kubeconfig`.
- The kubeconfig file contains authentication and cluster information.
- Save the kubeconfig file to `~/.kube/config` with `kind get kubeconfig --name wicked-demo > ~/.kube/config`.
- Having the kubeconfig file in `~/.kube/config` allows easy switching between clusters.
- The kubeconfig file includes the cluster's API server address, authentication credentials, and context.
- It is used by Kubernetes clients like `kubectl` to connect and interact with the cluster.
- Simplifies managing multiple clusters across different providers or environments.

### Customizable Resources with Kustomize (kuctl)

To customize resources with Kustomize, follow these steps:

#### Install Kustomize

```bash
sudo apt-get install -y kustomize
```

#### Build Kustomize Configuration

```bash
kustomize build <directory>
```

**Tip:** Apply the kustomization directly to the cluster.

```bash
kustomize build <directory> | kubectl apply -f -
```

### Monitoring and Observability Setup

To set up monitoring and observability, follow these steps:

#### Deploy Grafana and OpenTelemetry

```bash
helmfile -f helmfile.d/prod.yaml apply
```

#### Access Grafana UI

```bash
kubectl port-forward service/grafana 3000:80
```

**Tip:** Login with default credentials (`admin`/`admin`) and set up data sources.

### Validate ClearML Deployment

To validate the ClearML deployment, follow these steps:

#### Port-forward ClearML Server

```bash
kubectl port-forward service/clearml-webserver 8080:80
```

#### Access ClearML UI

Navigate to `http://localhost:8080` in a browser.

**Prober:**

#### Check ClearML Server Logs

```bash
kubectl logs -l app=clearml-webserver
```

**Tip:** Inspect environment-specific configurations.

```bash
helm get values clearml --namespace default
```

### Terraform for AWS Infrastructure (Production Only)

To set up Terraform for AWS infrastructure, follow these steps:

#### Apply Terraform Configuration

```bash
terraform -chdir=terraform/prod apply
```

#### Verify EKS Cluster Creation

```bash
aws eks describe-cluster --name <cluster-name>
```

**Prober:**

#### Check if EKS Cluster Nodes are Ready

```bash
kubectl get nodes
```

### Deploy to AWS EKS with Helmfile

To deploy to AWS EKS with Helmfile, follow these steps:

#### Switch Context to EKS Cluster

```bash
aws eks update-kubeconfig --name <cluster-name> --region <region>
```

#### Apply Helmfile for Production

```bash
helmfile -f helmfile.d/prod.yaml apply
```

**Prober:**

#### View All Kubernetes Resources

```bash
kubectl get all -n <namespace>
```

**Tip:** Check the status of all pods.

```bash
kubectl get pods -A
```

### Clean Up

To clean up, follow these steps:

#### Delete Kind Cluster

```bash
kind delete cluster --name wicked-demo
```

#### Destroy Terraform-managed AWS Resources

```bash
terraform -chdir=terraform/prod destroy
```

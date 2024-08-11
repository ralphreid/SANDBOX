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

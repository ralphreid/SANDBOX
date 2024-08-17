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

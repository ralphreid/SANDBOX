# minicube

## References

1. https://minikube.sigs.k8s.io/docs/start/
2. font


## Kubernetes

### kubctl

1. https://www.interviewbit.com/blog/kubectl-commands/
2. https://linuxhint.com/kubectl-top/
3. https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide/
4. https://kubernetes.io/docs/reference/kubectl/cheatsheet/
5. https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/

```bash
minikube master % kubectl get po -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS        AGE
kube-system   coredns-6d4b75cb6d-vdzdg           1/1     Running   0               3m58s
kube-system   etcd-minikube                      1/1     Running   0               4m16s
kube-system   kube-apiserver-minikube            1/1     Running   0               4m9s
kube-system   kube-controller-manager-minikube   1/1     Running   0               4m11s
kube-system   kube-proxy-k286c                   1/1     Running   0               3m59s
kube-system   kube-scheduler-minikube            1/1     Running   0               4m9s
kube-system   storage-provisioner                1/1     Running   1 (3m28s ago)   4m5s
```

```bash
kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4
kubectl expose deployment hello-minikube --type=NodePort --port=8080

kubectl get services hello-minikube

minikube service hello-minikube

kubectl port-forward service/hello-minikube 7080:8080

kubectl create deployment balanced --image=k8s.gcr.io/echoserver:1.4
kubectl expose deployment balanced --type=LoadBalancer --port=8080

minikube tunnel
kubectl get services balanced

minikube pause
minikube unpause

minikube stop
minikube config set memory 16384

minikube config set memory 16384
minikube addons list

minikube start -p aged --kubernetes-version=v1.16.1

```

```bash
minikube dashboard
minikube dashboard --url

kubectl get deployments
```

```bash
kubectl create -f test.yaml
```

```bash

```

```bash

```


## Nginx


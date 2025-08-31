# Personal Portfolio
> Welcome to my portfolio website! This is my personal portfolio—highlighting my career aspirations, academic background, professional journey, and key milestones.


## Run the project kubernetes cluster:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

> Check:
```bash
kubectl get pods
kubectl get svc
```


###### K8S port-forward

```bash
kubectl port-forward service/portfolio-service 8080:80
```

> URL:
```url
http://localhost:8080
```

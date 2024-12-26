# k8s fastapi

```bash 
docker build -t my-fastapi:latest -f backend/Dockerfile backend

kubectl apply -f postgres.yml
kubectl apply -f fastapi.yml
kubectl apply -f nginx.yml

kubectl apply -f ingress.yml


minikube tunnel


```
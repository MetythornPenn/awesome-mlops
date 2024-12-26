# Minikube


```bash
# start minikube
minikube start 

#Advanced start 
minikube start --driver docker 

# check status
minikube status

# open webui
minikube daskboard

# list all node 
kubectl get node


```

```bash
# create mongo-user & mongo-password for mongo-secret.yaml
echo -n mongouser | base64
echo -n mongopassword | base64
```


## Resource 
- [youtube tutorial](https://www.youtube.com/watch?v=s_o8dwzRlu4&t=104s)
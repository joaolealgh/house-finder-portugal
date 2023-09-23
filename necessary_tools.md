# Necessary tools to run the program:

0. WSL 2

Follow the instructions here:

https://learn.microsoft.com/en-us/windows/wsl/install

1. Docker

Follow the instructions here:

https://docs.docker.com/engine/install/ubuntu/

Start docker service:
`sudo service docker start`

Fix docker permissions:
`sudo chmod 666 /var/run/docker.sock`

---

2. Kubernetes

Installation of kubernetes with minikube:

More information here (https://minikube.sigs.k8s.io/docs/start/)

`curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64`

`sudo install minikube-linux-amd64 /usr/local/bin/minikube`

`minikube start`

`kubectl get po -A`

Start minikube dashboard:

`minikube dashboard`

(Optional) Install k9s to manage clusters:

`curl -sS https://webinstall.dev/k9s | bash`

To start k9s run:

`k9s`

---

3. Python >=3.8


4. Kafka

https://dzone.com/articles/how-to-deploy-apache-kafka-with-kubernetes

kubectl apply -k ./


add `127.0.0.1	kafka-broker` to /etc/hosts

Currently it is needed to Port forward kafka-broker to localhost:9092 -> change this in the future

Check why kafka ui isnt connecting to the broker: https://github.com/provectus/kafka-ui

Change the spark images to official images: https://github.com/kubernetes/examples/tree/master/staging/spark

kubectl apply -k ./ --namespace=spark-cluster

Run minikube tunnel to be able to connect to spark-ui-proxy in: http://localhost/proxy:spark-master:8080

Verify best way to deploy a postgres cluster in kubernetes (without replication, not necessary in this types of project)
- https://kodekloud.com/blog/deploy-postgresql-kubernetes/#setting-up-a-kubernetes-cluster 
- https://www.sumologic.com/blog/kubernetes-deploy-postgres/
- https://github.com/reactive-tech/kubegres -> too much fluff, unecessary replication for a local development
- https://gist.github.com/ivanbrennan/cf20e26de6e7cbf517d101e7cc9d4ca0

https://trello.com/b/d8Ki5pCN/house-finder-project

Test the connection as followed:
https://gist.github.com/ivanbrennan/cf20e26de6e7cbf517d101e7cc9d4ca0

# test the connection from within the cluster
url=$(kubectl --context=minikube get service postgres \
              --output=jsonpath='{.spec.clusterIP}:{.spec.ports[0].port}')
kubectl --context=minikube run pgbox --image=postgres:9.6 \
    --rm -it --restart=Never -- \
    bash -c "read &&
             psql --host=${url%:*} --port=${url#*:} \
                  --username=postgres --dbname=postgres \
                  --command='SELECT refobjid FROM pg_depend LIMIT 1'"


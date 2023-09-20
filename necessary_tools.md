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

Change the spark images to official images



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

- Using kafka confluence and json serializers to pass information between the Producer(Web crawler/Web scraper) and the Consumer(Pyspark node), it is necessary to setup multiple tools:
    - Kafka (confluent-kafka/docker-compose.yaml)
    - Schema registry (on premises)
    - Producer
    - Consumer

start the Kafka broker:
`docker compose up -d`

`curl -sL --http1.1 https://cnfl.io/cli | sh -s -- latest`


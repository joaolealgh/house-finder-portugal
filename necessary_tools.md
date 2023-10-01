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

---

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

Trello: https://trello.com/b/d8Ki5pCN/house-finder-project

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

# Connect to the postgres cluster using port forward and psql

1. Port forward using the k9s or `kubectl port-forward pod/postgresql-0 5432:5432`

2. `psql --host localhost --username postgres`

# Create a database and the tables in the postgres cluster

create-db-job.yaml inside /postgresql/manifests/

# Connect to the database using DBeaver
1. Port forward 
2. Connect to dbeaver using the correct url and credentials

# Copy pyspark.py to spark master container to test the script using spark-submit
`kubectl cp projects/house-finder-portugal/pyspark/src/batching_data.py default/spark-master-8d545cb67-j2xbr:batching_data.py`

# Test the script
`spark/bin/spark-submit --jars spark/jars/kafka-clients-3.3.0.jar batching_data.py`
`spark/bin/spark-submit batching_data.py` -> if the jars are already on the config in the consumer

https://github.com/big-data-europe/docker-spark/tree/master/template/python

kafka ui local:
https://gist.github.com/ashishmaurya/e192cdf44fdeeb459f0bfa09877dee22

How to deploy applications with spark submit: 
https://github.com/big-data-europe/docker-spark#kubernetes-deployment

Run spark shell:
`kubectl run spark-base --rm -it --labels="app=spark-client" --image bde2020/spark-base:3.3.0-hadoop3.3 -- bash ./spark/bin/spark-shell --master spark://spark-master:7077 --conf spark.driver.host=spark-client`

Run spark submit:
With class:
`kubectl run spark-base --rm -it --labels="app=spark-client" --image bde2020/spark-base:3.3.0-hadoop3.3 -- bash ./spark/bin/spark-submit --class CLASS_TO_RUN --master spark://spark-master:7077 --deploy-mode client --conf spark.driver.host=spark-client URL_TO_YOUR_APP`

Without class:
`kubectl run spark-base --rm -it --labels="app=spark-client" --image bde2020/spark-base:3.3.0-hadoop3.3 -- bash ./spark/bin/spark-submit --master spark://spark-master:7077 --deploy-mode client --conf spark.driver.host=spark-client URL_TO_YOUR_APP`

Spark with airflow: https://medium.com/swlh/using-airflow-to-schedule-spark-jobs-811becf3a960


(To do):
https://medium.com/go-city/deploying-apache-airflow-on-kubernetes-for-local-development-8e958675585d

Currently, using the helm chart of airflow to test if everything works well with spark:
https://airflow.apache.org/docs/helm-chart/stable/index.html

Installing the chart:
`helm repo add apache-airflow https://airflow.apache.org`
`helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace`

Uninstalling the chart:
`helm delete airflow --namespace airflow`
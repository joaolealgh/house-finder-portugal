# Decisions and though-processes taken during the project development

1. The initial though was to start by scraping all of the available real state websites that are most commonly known in the portuguese real state market.
    - There are two main problems with this, not including the additional development time that the web crawling/web scraping that would be needed since each website handles their html files differently:
        1. The first is that since this would be running on premises, which currently, just means that it would run local on a single pc, it would create memory consumption and processing power that would probably exceed the amount that is available for this project. In the future, however, this could be probably handled if the services were to be hosted in a cloud service, such as AWS, GCP, Azure, etc. In order to mitigate this, only one website was chosen to web scrape: http://supercasa.pt

        2. The amount of information that would be gathered would probably way too much to handle. Since there a lot more steps after the web crawling step, saving real state information from multiple sites (originally were 5 real state websites) there would be way too much data for a good analysis and understanding the data would take a long time. Similar to the first problem, in the future, the data could be saved into a cloud storage which would reduce the storage requirements that are necessary.

2. The communication between the web scraping/web crawling service and the pyspark service will be done using Kafka messaging. There are currently 3 main implementations of kafka for python:
    - Kafka-Python
    - PyKafka
    - Confluent Kafka Python

    1. The lib to use will be confluent kafka due to being maintained by confluent and being faster than the other libraries.
        - Problems with the confluence kafka
            - The current machine doesn't handle the amount of memory and cpu resources that is needed to run smoothly. And since the objective is to use kubernetes to deploy all the services/applications, a change must be made. The original kafka will be used.
            - Instructions followed to deploy CFK (https://docs.confluent.io/operator/current/co-quickstart.html#)

3.  Spark
    1. https://github.com/bitnami/charts/tree/main/bitnami/spark -> Uses helm chart 
    2. https://github.com/big-data-europe/docker-spark -> Doesnt use helm chart
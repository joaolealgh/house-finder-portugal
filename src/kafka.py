from confluent_kafka import Producer
import socket

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def start_producer():
    conf = {
    'bootstrap.servers': "localhost:9092",
    'client.id': socket.gethostname()
    }

    producer = Producer(conf)

    return producer

def send_message(producer: Producer, topic_name: str):
    producer.produce("SomeTopic", key="key1", value="Hello", callback=acked)     
    producer.poll(1)   # Maximum time (1s) to block while waiting for events

from abc import ABC
import json
import logging

from kafka import KafkaProducer
from kafka.errors import KafkaError

# TODO Make a class with Producer    

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    logging.error('I am an errback', exc_info=excp)
    # handle exception
    # TODO

def start_producer(bootstrap_servers=['localhost:9092']):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    return producer

def serialize_message(message: dict):
    return json.dumps(message).encode('utf-8')

def send_json_message(producer: KafkaProducer, topic: str, message: dict):
    message = serialize_message(message)
    producer.send(topic, message).add_callback(on_send_success).add_errback(on_send_error)
    # producer.flush()

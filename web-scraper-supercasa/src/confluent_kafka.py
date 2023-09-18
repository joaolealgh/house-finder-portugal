from uuid import uuid4
from confluent_kafka import Producer
from confluent_kafka.serialization import SerializationContext, MessageField, StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import socket

class SupercasaHouse(object):
    def __init__(self, link, title, price, location, features, highlights, description_text) -> None:
        self.link = link
        self.title = title
        self.price = price
        self.location = location
        self.features = features
        self.highlights = highlights
        self.description_text = description_text


def supercasahouse_to_dict(supercasahouse, ctx):
    return dict(link=supercasahouse.link,
                title=supercasahouse.title,
                price=supercasahouse.price,
                location=supercasahouse.location,
                features=supercasahouse.features,
                highlights=supercasahouse.highlights,
                description_text=supercasahouse.description_text
                )

def delivery_report(err, event):
    if err is not None:
        print(f'Delivery failed on reading for {event.key().decode("utf8")}: {err}')
    else:
        print(f'Temp reading for {event.key().decode("utf8")} produced to {event.topic()}')

def start_producer(bootstrap_servers='localhost:9092'):
    producer = Producer({'bootstrap.servers': bootstrap_servers})

    return producer

def send_message(producer: Producer, topic: str, supercasahouse: SupercasaHouse):
    schema_str = """
    {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Supercasa House",
        "description": "House details from an house in supercasa.pt website",
        "type": "object",
        "properties": {
            "link": {
                "description": "Website link of the house",
                "type": "string"
            },
            "title": {
                "description": "House title",
                "type": "string"
            },
            "price": {
                "description": "House price",
                "type": "string"
            },
            "features": {
                "description": "House features",
                "type": "string"
            },
            "highlights": {
                "description": "House highlights in the website",
                "type": "string"
            },
            "description_text": {
                "description": "Additional house information in the website",
                "type": "string"
            }
        }
    }
    """

    sr_config = {
        'url': '',
    }

    schema_registry_client = SchemaRegistryClient(sr_config)

    json_serializer = JSONSerializer(schema_str,
                                     schema_registry_client,
                                     supercasahouse_to_dict)

    string_serializer = StringSerializer('utf_8')

    key = string_serializer(str(uuid4())),
    
    producer.poll(1)   # Maximum time (1s) to block while waiting for events
    producer.produce(topic=topic,
                     key=key,
                     value=json_serializer(supercasahouse, SerializationContext(topic, MessageField.VALUE)),
                     on_delivery=delivery_report)     

    # print("\nFlushing records...")
    # producer.flush()


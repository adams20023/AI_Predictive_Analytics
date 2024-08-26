# scripts/kafka_producer.py
from kafka import KafkaProducer
import json

def produce_data(topic, data):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send(topic, data)
    producer.flush()


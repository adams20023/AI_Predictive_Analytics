# scripts/kafka_consumer.py
from kafka import KafkaConsumer
import json

def consume_data(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092',
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for message in consumer:
        process_data(message.value)


import json
from kafka import KafkaProducer

# Kafka setup
KAFKA_BROKER = "localhost:9092"  # Adjust as needed
KAFKA_TOPIC = "kafka_topic"  # Replace with your topic

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
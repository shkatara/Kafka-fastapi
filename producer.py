from kafka import KafkaProducer
from json import dumps
from dotenv import dotenv_values
from fake import fake_gen

config = dotenv_values(".env")

producer = KafkaProducer(
    bootstrap_servers=config['KAFKA_ADDRESS'],
    security_protocol="SSL",
    ssl_cafile="./secrets/ca.pem",
    ssl_certfile="./secrets/service.cert",
    ssl_keyfile="./secrets/service.key",
    value_serializer=lambda v: dumps(v).encode('ascii'), 
    key_serializer=lambda v: dumps(v).encode('ascii'), 
)

def produce_message():
    producer.send(
        'hotel-booking-request', 
        value = fake_gen()
    )    
    producer.flush()

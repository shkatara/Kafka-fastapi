from kafka import KafkaProducer
from json import dumps
from dotenv import dotenv_values
from fake import fake_gen
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

config = dotenv_values(".env")

@app.get("/produce")
def produce():
    producer = KafkaProducer(
    bootstrap_servers=config['KAFKA_ADDRESS'],
    security_protocol="SSL",
    ssl_cafile="./secrets/ca.pem",
    ssl_certfile="./secrets/service.cert",
    ssl_keyfile="./secrets/service.key",
    value_serializer=lambda v: dumps(v).encode('ascii'), 
    key_serializer=lambda v: dumps(v).encode('ascii'), 
    )

    producer.send(
        'hotel-booking-request', 
        value = fake_gen()
    )

    producer.flush()

if __name__ == "__main__":
   run("main:app", host="127.0.0.1", port=8000, reload=True,log_level="info")
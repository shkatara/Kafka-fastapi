from kafka import KafkaConsumer
from json import dumps,loads
from dotenv import dotenv_values
from time import sleep

config = dotenv_values(".env")

consumer = KafkaConsumer(
    'hotel-booking-request',
    bootstrap_servers=config['KAFKA_ADDRESS'],
    security_protocol="SSL",
    ssl_cafile="./secrets/ca.pem",
    ssl_certfile="./secrets/service.cert",
    ssl_keyfile="./secrets/service.key",
)

consumer.subscribe(topics="hotel-booking-request")
def main():
    try:
        for message in consumer:
            value = loads(message.value.decode('utf-8')) #result obtained from kafka is bytes type and has to be decoded to be a dictionary type to read specific keys from it
            print(
                f'Name: {value["name"]}',
                f'Address: {value["address"]}',
                f'Phone No: {value["phone_no"]}'
            )
    except KeyboardInterrupt:
        print("Got SIGINT. EXITING...")

if __name__ == "__main__":
    main()
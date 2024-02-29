
# Kafka Producer and Consumer with Python FastAPI

The repo holds a learning project that helps understanding of writing kafka producers and consumers in python with FastAPI. API can be used to produce a message to the kafka topic and the consumers can then be used to read the messages from the queue. 

\
This project serves as a self learning to have a better understanding of APIs and to be working with Apache Kafka cluster.

Along the way of this project, it uses:
1. Python 3.9.6 (Obviously)
1. FastAPI
2. kafka-python 
3. Faker

\

Install the project with pip. I recommend using python a virtual environment. Any changes to the code will result on a real-time reload of the uvicron engine and the changes are reflected in real time.

\
To start the producer API:
```bash
    git clone https://github.com/shkatara/Kafka-fastapi.git
    python -m venv venv
    . venv/bin/activate
    cd Kafka-fastapi
    pip install -r requirements.txt
    python main.py
```


\
On terminal 1, start the first consumer
```bash
   python consumer.py
```

\
On terminal 2, start the second consumer
```bash
   python consumer1.py
```

\
Once both the consumers are started, send the data to producer
```bash
   curl 127.0.0.1/8000/produce
```

\
If it is all good, we should see both the consumers printing out the message that was sent to the Kafka topic. This proves we can send messages to multiple services at the same time in Kafka. 

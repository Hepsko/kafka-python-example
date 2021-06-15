import random
import kafka.errors
from kafka import KafkaProducer
import json
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

run = False

while run != True:
    try:
        producer = KafkaProducer(bootstrap_servers=['broker:9092'],
                         value_serializer= json_serializer)
        run=True
    except kafka.errors.NoBrokersAvailable as e:
        pass
       # print("waiting for broker")


if __name__ == "__main__":
    while 1 == 1:
        temp = random.randint(0, 1000)/10
        print("Temperature: " + str(temp))
       	producer.send("temperature", temp)
        time.sleep(random.randint(0,10))

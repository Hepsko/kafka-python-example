import kafka.errors
from kafka import KafkaConsumer
import json
import time


run = False
consumer = None
if __name__ == "__main__":
    while run != True:
        try:
            consumer = KafkaConsumer(
                "temperature",
                bootstrap_servers='172.20.0.3:9092',
                auto_offset_reset='earliest',
                group_id="consumer-group-a")
            print("consumer start")
            run = True
        except kafka.errors.NoBrokersAvailable as e:
            print("Waiting for broker")

    for msg in consumer:
        print("Consumer: Temperature: " + str(msg.value) )



import kafka.errors
from kafka import KafkaConsumer
import mysql.connector

db = False


while db!= True:

    try:
        connect = mysql.connector.connect(
            host="database",
            user="dockerdb",
            password="adrian",
            auth_plugin='mysql_native_password',
            database="baza")
        db=True
    except mysql.connector.Error as e:
        pass

run = False
consumer = None
if __name__ == "__main__":
    while run != True:
        try:
            consumer = KafkaConsumer(
                "temperature",
                bootstrap_servers='broker:9092',
                auto_offset_reset='earliest',
                group_id="consumer-group-a")
            print("consumer start")
            run = True
        except kafka.errors.NoBrokersAvailable as e:
            pass
            #print("Waiting for broker")
    counter = 0
    sum=0
    for msg in consumer:
        cursor = connect.cursor()
        print("Consumer: Temperature: " + str(msg.value) )
        try:
            sum+=   float(msg.value)
            counter+=1
        except ValueError:
            pass
        if counter >= 10:
            AVG= (sum/10)
            AVG = round(AVG,2)
            sum=0
            counter=0
            cursor.execute("INSERT INTO baza.tabela(temperature, date_with_time) VALUES ( %s, CURRENT_TIMESTAMP())", (AVG,))
            print("Avrage temperature has been added to database: " + str(AVG))
            connect.commit()
            cursor.close()
    connect.close()
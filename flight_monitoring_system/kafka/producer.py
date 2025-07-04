from kafka import KafkaProducer
import json
import time
import random

KAFKA_TOPIC = 'flight_data'
KAFKA_BROKER = 'localhost:29092'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_flight_data(anomaly_chance=0.2):
    altitude = random.uniform(3000, 40000)
    speed = random.uniform(200, 500)

    if random.random() < anomaly_chance:
        
        if random.choice(['altitude', 'speed']) == 'altitude':
            altitude = random.choice([random.uniform(0, 2999), random.uniform(40001, 50000)])
        else:
            speed = random.choice([random.uniform(0, 199), random.uniform(501, 600)])
    return {
        'altitude': altitude,
        'speed': speed,
        'timestamp': time.time()
    }

if __name__ == "__main__":
    print("Starting kafka producer...")
    max_records = 10000
    sent_records = 0
    while sent_records < max_records:   
        data = generate_flight_data()  
        print(f"Sending data: {data}")

        producer.send(KAFKA_TOPIC, value=data)  
        producer.flush()                        

        sent_records += 1  
        time.sleep(1)
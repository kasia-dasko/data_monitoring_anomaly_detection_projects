from kafka import KafkaConsumer
import json
import csv
import os

consumer = KafkaConsumer(
    'flight_data',
    bootstrap_servers='localhost:29092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

MIN_ALTITUDE = 3000
MAX_ALTITUDE = 40000
MIN_SPEED = 200
MAX_SPEED = 500

print("Kafka consumer started. Waiting for data...")

CSV_FILE = 'flight_data.csv'

if not os.path.isfile(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'altitude', 'speed', 'alert'])

for message in consumer:
    data = message.value
    altitude = data.get('altitude')
    speed = data.get('speed')
    timestamp = data.get('timestamp')

    alert = ""

    print(f"Received: Altitude={altitude:.1f} ft | Speed={speed:.1f} knots")

    if altitude < MIN_ALTITUDE:
        print("ALERT: Altitude below safe threshold!")
    elif altitude > MAX_ALTITUDE:
        print("ALERT: Altitude above safe threshold!")

    if speed < MIN_SPEED:
        print("ALERT: Speed below safe threshold!")
    elif speed > MAX_SPEED:
        print("ALERT: Speed above safe threshold!")

with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, altitude, speed, alert])
    

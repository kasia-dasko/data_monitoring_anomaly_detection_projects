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

CSV_FILE = os.path.abspath('flight_data.csv')
print(f"CSV file will be created at: {CSV_FILE}")

if not os.path.isfile(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'altitude', 'speed', 'alert'])

for message in consumer:
    data = message.value
    altitude = data.get('altitude')
    speed = data.get('speed')
    timestamp = data.get('timestamp')

    alert_messages = []

    print(f"Received: Altitude={altitude:.1f} ft | Speed={speed:.1f} knots")

    if altitude < MIN_ALTITUDE:
        alert_messages.append("Altitude below safe threshold")
        print("ALERT: Altitude below safe threshold!")
    elif altitude > MAX_ALTITUDE:
        alert_messages.append("Altitude above safe threshold")
        print("ALERT: Altitude above safe threshold!")

    if speed < MIN_SPEED:
        alert_messages.append("Speed below safe threshold")
        print("ALERT: Speed below safe threshold!")
    elif speed > MAX_SPEED:
        alert_messages.append("Speed above safe threshold")
        print("ALERT: Speed above safe threshold!")

    alert = "; ".join(alert_messages) if alert_messages else "No alert"

    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, altitude, speed, alert])
    

from kafka import KafkaConsumer
import json

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

for message in consumer:
    data = message.value
    altitude = data.get('altitude')
    speed = data.get('speed')

    print(f"Received: Altitude={altitude:.1f} ft | Speed={speed:.1f} knots")

    if altitude < MIN_ALTITUDE:
        print("ALERT: Altitude below safe threshold!")
    elif altitude > MAX_ALTITUDE:
        print("ALERT: Altitude above safe threshold!")

    if speed < MIN_SPEED:
        print("ALERT: Speed below safe threshold!")
    elif speed > MAX_SPEED:
        print("ALERT: Speed above safe threshold!")
    

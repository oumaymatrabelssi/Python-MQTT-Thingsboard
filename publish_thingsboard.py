import paho.mqtt.publish as publish
import json


MQTT_HOST = "YOUR_IP_ADDRESS"
MQTT_PORT =  1883

# Get your device Acess Token from Thingsboard
ACCESS_TOKEN = "20kLSPXATUeTsbV1TG4l"
TOPIC = "v1/devices/me/telemetry"

# Data that will send 
PAYLOAD = {"temperature": 85, "humidity": 1500}

# Convert the payload to a json format
MQTT_MSG=json.dumps(PAYLOAD).encode('utf-8');
if __name__ == '__main__':
    # publish a single message
    publish.single(topic=TOPIC, payload=MQTT_MSG, hostname=MQTT_HOST, port=MQTT_PORT, qos=1, auth={'username': ACCESS_TOKEN})
    print("Message was published")

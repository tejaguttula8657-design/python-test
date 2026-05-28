import pandas as pd
import paho.mqtt.client as mqtt
import time
import json

# MQTT Details
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "topic"

# Create MQTT client
client = mqtt.Client()

# Connect
client.connect(BROKER, PORT, 60)

print("Connected to HiveMQ")

# Read CSV
data = pd.read_csv(r"C:\Users\Admin\Downloads\Impedance_Results.csv")

# Publish each row
for index, row in data.iterrows():

    message = {
        "Time": row["t_valid"],
        "Za_v": row["Za_v"],
        "Za_a": row["Za_a"],
        "Ra": row["Ra"],
        "Xa": row["Xa"],
        "Zb_v": row["Zb_v"],
        "Zb_a": row["Zb_a"],
        "Rb": row["Rb"],
        "Xb": row["Xb"],
        "Zc_v": row["Zc_v"],
        "Zc_a": row["Zc_a"],
        "Rc": row["Rc"],
        "Xc": row["Xc"]
    }

    payload = json.dumps(message)

    client.publish(TOPIC, payload)

    print("Published:", payload)

    time.sleep(1)

client.disconnect()

print("Finished Sending Data")
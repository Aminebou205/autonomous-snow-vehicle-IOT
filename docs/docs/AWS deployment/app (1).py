from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import json
import csv
import time
import threading

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
TOPIC = "snow/data"
CSV_FILE = "snow_terrain_mobility_raw.csv"

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()

app = Flask(__name__)

@app.route("/send", methods=["POST"])
def send_data():
    data = request.json
    mqtt_client.publish(TOPIC, json.dumps(data))
    return jsonify({"status": "sent", "data": data})

def stream_csv():
    while True:
        with open(CSV_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                mqtt_client.publish(TOPIC, json.dumps(row))
                print("Published:", row)
                time.sleep(1)

threading.Thread(target=stream_csv, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

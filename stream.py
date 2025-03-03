import json
import time
import random
from azure.eventhub import EventHubProducerClient, EventData

connection_str = "YOUR_EVENT_HUB_CONNECTION_STRING"
eventhub_name = "RealTimeDataHub"

producer = EventHubProducerClient.from_connection_string(conn_str=connection_str, eventhub_name=eventhub_name)

while True:
    data = {
        "DeviceId": "Device001",
        "Temperature": random.uniform(20, 35),
        "Humidity": random.uniform(30, 70)
    }
    event = EventData(json.dumps(data))
    with producer:
        producer.send_batch([event])
    print("Sent data: ", data)
    time.sleep(5)

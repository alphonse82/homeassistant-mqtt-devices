import uuid
from paho.mqtt.client import Client
import MQTTSensor

class MQTTThermometer(MQTTSensor.MQTTSensor):
    def __init__(self,
                 name: str,
                 node_id: str,
                 client: Client,
                 unit: str = "°C",
                 unique_id=str(uuid.uuid4()),
                 device_dict: dict = None):
        super().__init__(name, node_id, client, unit,"temperature", unique_id=unique_id,device_dict=device_dict)

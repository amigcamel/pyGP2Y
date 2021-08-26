from umqtt.simple import MQTTClient

from ha import config
import secrets


def set_auto_discovery():
    pass


def build_mqtt_connection():
    return MQTT(
        client_id=secrets.MQTT_CLIENT_ID,
        host=secrets.MQTT_HOST,
        port=secrets.MQTT_PORT,
        user=secrets.MQTT_USER,
        password=secrets.MQTT_PASSWORD,
    )


class MQTT:

    def __init__(self, client_id, host, port, user, password, keepalive=5):
        self.client = MQTTClient(client_id, host, port, user, password, keepalive)
        print("set last will")
        self.client.set_last_will(config["avty_t"], config["pl_not_avail"])
        self.client.connect()
        print('publish online')
        self.client.publish(config["avty_t"], config["pl_avail"])

    def __del__(self):
        self.client.disconnect()

from umqttsimple import MQTTClient

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

    def __init__(self, client_id, host, port, user, password):
        self.client = MQTTClient(client_id, host, port, user, password)
        self.client.connect()

    def __del__(self):
        self.client.disconnect()

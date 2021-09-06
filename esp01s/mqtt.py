import json

try:
    from umqtt.robust import MQTTClient
except ImportError:
    import upip

    upip.install("umqtt.simple")

from ha import config, conf
import secrets


class MQTT:
    def __init__(
        self,
        client_id=secrets.MQTT_CLIENT_ID,
        host=secrets.MQTT_HOST,
        port=secrets.MQTT_PORT,
        user=secrets.MQTT_USER,
        password=secrets.MQTT_PASSWORD,
        keepalive=60,
    ):
        self.client = MQTTClient(client_id, host, port, user, password, keepalive)
        print("set last will")
        self.client.set_last_will(config["avty_t"], config["pl_not_avail"])
        self.client.connect()
        print("send config")
        self.client.publish(conf.encode(), json.dumps(config).encode())
        print("publish online")
        self.client.publish(config["avty_t"].encode(), config["pl_avail"].encode())

    def __del__(self):
        self.client.disconnect()

    def update_state(self, message):
        self.client.publish(config["stat_t"].encode(), message)

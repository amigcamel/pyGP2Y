from dust import monitor
# from mqtt import build_mqtt_connection
# from ha import config
from display import Display


# mq = build_mqtt_connection()
dp = Display()


def callback(density):
    if density == 0:
        seq = "0.0"
    else:
        seq = str(round(density, 1))
    dp(seq)
    # mq.client.publish(config["stat_t"].encode(), seq.encode())


if __name__ == "__main__":
    monitor(callback=callback)

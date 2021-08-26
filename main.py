from dust import monitor
from mqtt import build_mqtt_connection
from ha import config

from TM74HC595 import TM74HC595Controller


display = TM74HC595Controller(
    sclk=0,  # D3
    rclk=4,  # D2
    dio=5,  # D1
    num_displays=4,
)

mq = build_mqtt_connection()


def callback(density):
    if density == 0:
        seq = "----"
    else:
        seq = str(density)[:5]
    display.show_sequence(seq, redraw=100)
    mq.client.publish(config["stat_t"], str(density))


if __name__ == "__main__":
    monitor(callback=callback)

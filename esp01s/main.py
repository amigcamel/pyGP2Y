import gc
import time

import uos
import esp

from mqtt import MQTT
from uart import receive
import wifi


if __name__ == "__main__":
    time.sleep(2)
    esp.osdebug(None)
    gc.collect()
    uos.dupterm(None, 1)  # TODO: what is "1"?
    wifi.connect()

    mq = MQTT()
    receive(callback=mq.update_state)

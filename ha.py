import os

import machine
import ubinascii

os_uname = os.uname()
uri = "homeassistant/sensor/dust"
acty_t = uri + "/avail"
stat_t = uri + "/state"
conf = uri + "/config"


config = {
    "name": "SharpDustSensor",
    "avty_t": acty_t,
    "stat_t": stat_t,
    "pl_avail": "online",
    "pl_not_avail": "offline",
    "ic": "mdi:grain",
    "unit_of_meas": "µg/m3",
    "uniq_id": "pygp2ydustsensor",
    "qos": 0,
    "dev": {
        "mdl": "gp2y1014au0f",
        "mf": "Sharp",
        "name": "SharpDustSensorv2",
        "ids": [
            ubinascii.hexlify(machine.unique_id()).decode(),
        ],
        "sw": "%s-%s (MicroPython)" % (os_uname.nodename, os_uname.version),
    },
}

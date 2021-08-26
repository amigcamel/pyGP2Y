import os

import machine

os_uname = os.uname()

config = {
    "name": "SharpDustSensor",
    "avty_t": "homeassistant/sensor/dust/avail",
    "stat_t": "homeassistant/sensor/dust/state",
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
            machine.unique_id(),
        ],
        "sw": "%s-%s (MicroPython)" % (os_uname.nodename, os_uname.version),
    },
}

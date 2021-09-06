import network

import secrets

from led import LED, blink


def connect():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(secrets.SSID, secrets.PASSWORD)
    LED.value(0)
    while not station.isconnected():
        print("Connecting...")
    LED.value(1)
    print("WIFI Connected.")
    print(station.ifconfig())
    blink(5)

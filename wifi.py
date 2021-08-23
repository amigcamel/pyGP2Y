import network

import secrets


def connect():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(secrets.SSID, secrets.PASSWORD)
    while not station.isconnected():
        print("Connecting...")
    print("WIFI Connected.")
    print(station.ifconfig())

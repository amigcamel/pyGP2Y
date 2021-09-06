from time import sleep

from machine import Pin

LED = Pin(2, Pin.OUT)


def blink(num):
    """Make on-board LED blink for N times."""
    for i in range(num * 2):
        sleep(0.05)
        LED.value(i % 2)
        sleep(0.05)

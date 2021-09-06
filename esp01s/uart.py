from machine import UART

from led import LED


def receive(callback):
    uart = UART(0)
    while True:
        msg = b""
        while uart.any():
            LED.value(0)
            msg += uart.read(1)
            LED.value(1)
        if msg:
            callback(msg)

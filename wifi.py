"""Connect to wifi with ESP-01s via UART.

Adopted from https://helloraspberrypi.blogspot.com/2021/02/connect-esp-01s-esp8266-to-raspberry-pi.html
"""
import board
import busio
import time


UART = busio.UART(board.GP0, board.GP1, baudrate=115200)


def send_at(cmd, timeout=2000):
    """Send AT command."""
    assert cmd.startswith("AT")
    cmd += "\r\n"
    print(f"CMD: {cmd}")
    UART.write(cmd.encode())
    prev_time = time.monotonic()
    resp = b""
    while ((time.monotonic() - prev_time) * 1000) < timeout:
        chr = UART.read(1)
        if chr:
            resp = b"".join([resp, chr])
    try:
        return resp
    except Exception:
        raise


def connect_to_wifi(ssid, password):
    """Connect to wifi."""
    send_at("AT")
    send_at("AT+CWMODE=1")  # set to station mode
    send_at(f'''AT+CWJAP="{ssid}","{password}"''', timeout=10000)

from machine import UART
from ucollections import deque
import _thread
# import gc

from dust import monitor
from display import Display


dp = Display()
queue = deque((), 2)
uart = UART(1)


def callback(density):
    if density == 0:
        seq = "0.0"
    else:
        seq = str(round(density, 1))
        queue.append(seq)
        uart.write(seq)


def _display():
    while True:
        # print(gc.mem_free())
        if queue:
            seq = queue.popleft()
            dp(seq)


if __name__ == "__main__":
    _thread.start_new_thread(_display, ())
    monitor(callback=callback)

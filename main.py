from dust import monitor
from TM74HC595 import TM74HC595Controller


display = TM74HC595Controller(
    sclk=0,  # D3
    rclk=4,  # D2
    dio=5,  # D1
    num_displays=4,
)


def callback(density):
    if density == 0:
        seq = "----"
    else:
        seq = str(density)[:5]
    display.show_sequence(seq, redraw=100)


if __name__ == "__main__":
    monitor(callback=callback)

from TM74HC595 import TM74HC595Controller


class Display:

    def __init__(self):
        self.display = TM74HC595Controller(
            sclk=6,
            rclk=7,
            dio=10,
            num_displays=4,
        )

    def __call__(self, seq, redraw=100):
        start_at = self.calc_start_at(seq)
        self.display.show_sequence(seq, redraw=redraw, start_at=start_at)

    def calc_start_at(self, seq):
        return self.display.num_displays - len(seq.replace(".", ""))

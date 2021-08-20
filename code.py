from time import sleep

from board import GP22, GP26
import analogio
import digitalio


# pin setup
LED_PIN = digitalio.DigitalInOut(GP22)
LED_PIN.direction = digitalio.Direction.OUTPUT
VO_PIN = analogio.AnalogIn(GP26)

# constants
SAMPLING_TIME = 0.00028
DELTA_TIME = 0.00004
SLEEP_TIME = 0.00968
VOC = 0.6
MAX = 0


def calc_volt(val):
    return val * 5 / 65536


def calc_density(vo, k=0.5):
    global VOC
    global MAX

    dv = vo - VOC
    if dv < 0:
        dv = 0
        VOC = vo
    density = dv / k * 100
    MAX = max(MAX, density)
    return density


def main(sample_size=100):
    vals = []
    while True:
        try:
            LED_PIN.value = 0
            sleep(SAMPLING_TIME)
            vals.append(VO_PIN.value)
            sleep(DELTA_TIME)
            LED_PIN.value = 1
            sleep(SLEEP_TIME)
            if len(vals) == sample_size:
                avg = sum(vals) / len(vals)
                volt = calc_volt(avg)
                density = calc_density(volt)
                print(f"{volt * 1000} mV / {density} ug/m3 (Voc={VOC}) | Max: {MAX} ug/m3")
                vals = []
        except KeyboardInterrupt:
            break
        except Exception:
            raise
        finally:
            LED_PIN.value = 0

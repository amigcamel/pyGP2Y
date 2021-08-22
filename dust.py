import machine
from time import sleep

# pin setup
LED_PIN = machine.Pin(16, machine.Pin.OUT)  # D0
VO_PIN = machine.ADC(0)  # A0

# constants
SAMPLING_TIME = 0.00028
DELTA_TIME = 0.00004
SLEEP_TIME = 0.00968
VOC = 0.6
MAX = 0


def calc_volt(val):
    return val * 3.3 / 1024


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


def monitor(sample_size=100, callback=None):
    vals = []
    while True:
        try:
            LED_PIN.value(0)
            sleep(SAMPLING_TIME)
            vals.append(VO_PIN.read())
            sleep(DELTA_TIME)
            LED_PIN.value(1)
            sleep(SLEEP_TIME)
            if len(vals) == sample_size:
                avg = sum(vals) / len(vals)
                volt = calc_volt(avg)
                density = calc_density(volt)
                mv = volt * 1000
                print(
                    "{mv} mV / {density} ug/m3 (Voc={voc}) | Max: {max_} ug/m3".format(  # noqa
                        mv=mv,
                        density=density,
                        voc=VOC,
                        max_=MAX,
                    )
                )
                vals = []
                if callback:
                    callback(density)
        except KeyboardInterrupt:
            break
        except Exception:
            raise
        finally:
            LED_PIN.value(0)

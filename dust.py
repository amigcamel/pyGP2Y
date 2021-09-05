import machine
import time

# pin setup
LED_PIN = machine.Pin(22, machine.Pin.OUT)
VO_PIN = machine.ADC(2)  # Pin 28

# constants
SAMPLING_TIME = 280
SLEEP_TIME = 10000 - SAMPLING_TIME
VOC = 0.6
MAX = 0


def calc_volt(val):
    return val * 5 / 65535


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
    counter = 0
    val = 0
    while True:
        try:
            LED_PIN.value(0)
            time.sleep_us(SAMPLING_TIME)
            t1 = time.ticks_us()
            val += VO_PIN.read_u16()
            counter += 1
            t2 = time.ticks_us()
            LED_PIN.value(1)
            time.sleep_us(SLEEP_TIME - (t2 - t1))
            if counter == sample_size:
                avg = val / sample_size
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
                val = 0
                counter = 0
                if callback:
                    callback(density)
        except KeyboardInterrupt:
            break
        except Exception:
            raise
        finally:
            LED_PIN.value(0)

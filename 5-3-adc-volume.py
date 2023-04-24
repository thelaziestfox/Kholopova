import RPi.GPIO as RP
import time

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]


def adc():
    s = 0
    for i in range(7, -1,-1):
        s += 2**i
        RP.output(dac, dec2bin(s))
        time.sleep(0.001)
        if RP.input(comp) == 0:
            s -= 2**i
    return s


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

RP.setmode(RP.BCM)
RP.setmode(dac, RP.OUT)
RP.setmode(leds, RP.OUT)
RP.setmode(troyka, RP.OUT, initial = RP.HIGH)
RP.setmode(comp, RP.IN)

try:
    while True:
        c = adc()
        RP.output(leds, dec2bin(c))
        voltage = c / 256 * 3.3
        if c != 0:
            print(c, voltage)
finally:
    RP.output(dac, 0)
    RP.cleanup()
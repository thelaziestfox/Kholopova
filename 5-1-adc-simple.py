import RPi.GPIO as RP

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]


def adc():
    for value in range(256):
        RP.output(dac, dec2bin(value))
        compv = RP.input(comp)
        return compv


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

RP.setmode(RP.BCM)
RP.setmode(dac, RP.OUT)
RP.setmode(troyka, RP.OUT, initial = RP.HIGH)
RP.setmode(comp, RP.IN)

try:
    while True:
        c = adc()
        voltage = c / 256 * 3.3
        print(c, voltage)
finally:
    RP.output(dac, 0)
    RP.cleanup()
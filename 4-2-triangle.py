import RPi.GPIO as RP
import time

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
RP.setmode(RP.BCM)
RP.setmode(dac, RP.OUT)

try:
    while True:
        a = input()
        if a == 'q':
            break
        elif a.isdigit() and int(a) % 1 == 0 and 0 <= int(a) <= 255:
            RP.output(dac, dec2bin(int(a)))
            print("{:.4f".format((int(a)/256)*3.3))
        else:
            for i in range(256):
                RP.output(dac, dec2bin(i))
                time.sleep(int(a)/512)
            for i in range(255, -1, -1):
                RP.output(dac, dec2bin(i))
                time.sleep(int(a)/512)
finally:
    RP.output(dac, 0)
    RP.cleanup()

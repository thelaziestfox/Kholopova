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

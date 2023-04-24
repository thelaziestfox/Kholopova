import RPi.GPIO as RP

RP.setmode(RP.BCM)
RP.setup(26, RP.OUT)

try:
    p = RP.PWM(26, 100)
    p.start(0)
    while True:
        k = int(input())
        p.start(k)
finally:
    p.stop()
    RP.cleanup()

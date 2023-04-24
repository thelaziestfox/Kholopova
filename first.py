import RPi.GPIO as RP

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
            print("input number [0, 255]")
except ValueError:
    print("input number [0, 255]")
except KeyboardInterrupt:
    print('OK')
finally:
    RP.output(dac, 0)
    RP.cleanup()
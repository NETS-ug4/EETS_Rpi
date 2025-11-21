import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class MUX:
    def __init__(self, a, b, c):
        self.pins = [a, b, c]
        for p in self.pins:
            GPIO.setup(p, GPIO.OUT)

    def select(self, ch):
        bits = format(ch, "03b")
        for pin, bit in zip(self.pins, bits):
            GPIO.output(pin, int(bit))

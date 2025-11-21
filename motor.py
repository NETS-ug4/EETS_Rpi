import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sequence = [
    [1,0,0,1],
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1]
]

class StepperMotor:
    def __init__(self, pins):
        self.pins = pins
        for p in pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, 0)

    def rotate_steps(self, steps):
        for i in range(steps):
            for step in sequence:
                for pin, val in zip(self.pins, step):
                    GPIO.output(pin, val)
                time.sleep(0.0018)

    def rotate_degree(self, degree):
        step_count = int(4096 * degree / 360)
        self.rotate_steps(step_count)

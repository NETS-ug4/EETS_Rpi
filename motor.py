import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Half-step sequence for 28BYJ-48 stepper motor
HALF_STEP_SEQ = [
    [1,0,0,1],
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1]
]

class ULN2003Stepper:
    def __init__(self, pins):
        self.pins = pins
        for p in pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, 0)

        self.steps_per_rev = 4096  # 28BYJ-48 standard

    def cleanup(self):
        for p in self.pins:
            GPIO.output(p, 0)
        GPIO.cleanup()

    def move(self, direction, speed, angle):
        """
        direction: "CW" or "CCW"
        speed: 1 to 10 (higher = faster)
        angle: degrees to rotate
        """

        # Speed control: convert speed (1–10) → delay (slow → fast)
        delay = 0.0025 - (speed * 0.0002)
        if delay < 0.0005:
            delay = 0.0005

        # Calculate number of steps
        step_count = int(self.steps_per_rev * angle / 360)

        # Decide direction
        seq = HALF_STEP_SEQ if direction == "CW" else HALF_STEP_SEQ[::-1]

        # Run motor
        for _ in range(step_count):
            for step in seq:
                for pin, val in zip(self.pins, step):
                    GPIO.output(pin, val)
                time.sleep(delay)

import RPi.GPIO as GPIO
import time
import random


class LaserMUX:
    def __init__(self, S0, S1, S2, S3, SIG_PIN, EN_PIN, num_leds=16):
        GPIO.setmode(GPIO.BCM)

        self.S0 = S0
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
        self.SIG_PIN = SIG_PIN
        self.EN_PIN = EN_PIN
        self.num_leds = num_leds

        self.current_channel = -1

        # Setup pins
        GPIO.setup(self.S0, GPIO.OUT)
        GPIO.setup(self.S1, GPIO.OUT)
        GPIO.setup(self.S2, GPIO.OUT)
        GPIO.setup(self.S3, GPIO.OUT)
        GPIO.setup(self.SIG_PIN, GPIO.OUT)
        GPIO.setup(self.EN_PIN, GPIO.OUT)

        # Enable MUX (active LOW)
        GPIO.output(self.EN_PIN, GPIO.LOW)

        # Keep signal ON
        GPIO.output(self.SIG_PIN, GPIO.HIGH)

        print("MUX Initialized")

    def select_channel(self, channel):
        """Select one of 16 channels (C1–C16)"""
        GPIO.output(self.S0, channel & 0x01)
        GPIO.output(self.S1, (channel >> 1) & 0x01)
        GPIO.output(self.S2, (channel >> 2) & 0x01)
        GPIO.output(self.S3, (channel >> 3) & 0x01)

    def pick_random_led(self):
        """Select a random LED different from previous"""
        new_channel = random.randint(0, self.num_leds - 1)

        while new_channel == self.current_channel:
            new_channel = random.randint(0, self.num_leds - 1)

        self.current_channel = new_channel
        mux_channel = new_channel + 1   # C1–C16

        self.select_channel(mux_channel)

        print(f"LED Index: {new_channel}  →  MUX Channel: C{mux_channel}")

        return mux_channel

    def cleanup(self):
        GPIO.cleanup()

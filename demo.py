from mux import LaserMUX
import time

# Your pin configuration
mux = LaserMUX(
    S0=25,
    S1=8,
    S2=7,
    S3=1,
    SIG_PIN=12,
    EN_PIN=0,
    num_leds=16
)

try:
    while True:
        mux.pick_random_led()
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
    mux.cleanup()

import tkinter as tk
from motor import StepperMotor
from buzzer import Buzzer
from mux import MUX

# Initialize devices
motor1 = StepperMotor([4, 17, 27, 22])
motor2 = StepperMotor([5, 6, 13, 19])
buzzer = Buzzer(23)
mux = MUX(20, 21, 26)

# --- Actions ---
def rotate_60():
    motor1.rotate_degree(60)

def rotate_20():
    motor2.rotate_degree(20)

def buzzer_on():
    buzzer.on()

def buzzer_off():
    buzzer.off()

def mux_channel(ch):
    mux.select(ch)

# --- GUI ---
root = tk.Tk()
root.title("Raspberry Pi Control Panel")
root.geometry("400x600")

tk.Label(root, text="STEPPER CONTROL", font=("Arial", 18, "bold")).pack(pady=10)

tk.Button(root, text="Motor 1 → 60°", font=("Arial", 16), width=20,
          command=rotate_60).pack(pady=10)

tk.Button(root, text="Motor 2 → 20°", font=("Arial", 16), width=20,
          command=rotate_20).pack(pady=10)

tk.Label(root, text="BUZZER", font=("Arial", 18, "bold")).pack(pady=20)

tk.Button(root, text="Buzzer ON", font=("Arial", 16), width=20,
          command=buzzer_on).pack(pady=10)

tk.Button(root, text="Buzzer OFF", font=("Arial", 16), width=20,
          command=buzzer_off).pack(pady=10)

tk.Label(root, text="MUX SELECT", font=("Arial", 18, "bold")).pack(pady=20)

for i in range(8):
    tk.Button(root, text=f"Channel {i}", font=("Arial", 14), width=15,
              command=lambda ch=i: mux_channel(ch)).pack(pady=5)

root.mainloop()

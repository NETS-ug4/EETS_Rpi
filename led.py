import RPi.GPIO as GPIO
import tkinter as tk
import time

# GPIO setup
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Tkinter GUI setup
root = tk.Tk()
root.title("LED Control")
root.geometry("300x200")

def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    status.config(text="LED is ON", fg="green")

def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    status.config(text="LED is OFF", fg="red")

# GUI layout
label = tk.Label(root, text="LED Controller", font=("Arial", 20))
label.pack(pady=10)

on_btn = tk.Button(root, text="Turn ON", font=("Arial", 18),
                   bg="#4CAF50", fg="white", width=10,
                   command=led_on)
on_btn.pack(pady=5)

off_btn = tk.Button(root, text="Turn OFF", font=("Arial", 18),
                    bg="#F44336", fg="white", width=10,
                    command=led_off)
off_btn.pack(pady=5)

status = tk.Label(root, text="LED is OFF", font=("Arial", 16), fg="red")
status.pack(pady=10)

def on_close():
    GPIO.cleanup()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()

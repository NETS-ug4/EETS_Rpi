import RPi.GPIO as GPIO
import tkinter as tk
from datetime import datetime
from motor import ULN2003Stepper
import time
from PIL import Image, ImageTk  # FIX

# Variable 
count = 1

# -----------------------------
# GPIO Setup
# -----------------------------

# Initialize devices
motor1 = ULN2003Stepper([4, 17, 27, 22])
motor2 = ULN2003Stepper([5, 6, 13, 19])

# -----------------------------
# Basic Button Functions
# -----------------------------

# ---------------------z--------
# Button Motor Functions
# -----------------------------
def previous_module():
    print("Motor rotate 60 degree Backward")
    global count
    if count > 1:
        count -= 1
    else:      # count == 1
        count = 6
    game_status.config(text=f"Game : {count}", fg="green",font=("Arial", 12, "bold"))
    motor1.move("CCW", 5, 60)   # clockwise, medium speed, 90 degrees
    time.sleep(1)

def next_module():
    print("Motor rotate 60 degree Forward")
    global count
    if count < 6:
        count += 1
    else:
        count = 1
    game_status.config(text=f"Game : {count}", fg="green",font=("Arial", 12, "bold"))
    motor1.move("CW", 5, 60)   # clockwise, medium speed, 90 degrees
    time.sleep(1)

def back15():
    print("Motor rotate 15 degree Backward")
    motor1.move("CCW", 5, 15)   # clockwise, medium speed, 90 degrees
    time.sleep(1)

def next15():
    print("Motor rotate 15 degree Forward")
    motor1.move("CW", 5, 15)   # clockwise, medium speed, 90 degrees
    time.sleep(1)

def up_module():
    print("Motor UP")
    motor2.move("CW", 6, 20)   # clockwise, medium speed, 90 degrees
    time.sleep(1)

def down_module():
    print("Motor DOWN")
    motor2.move("CCW", 6, 20)   # clockwise, medium speed, 90 degrees
    time.sleep(1)

# -----------------------------
# Window Setup
# -----------------------------
root = tk.Tk()
root.geometry("950x550")
root.configure(bg="#003153")
# -----------------------------
# Add LOGO + App Title
# -----------------------------
logo = Image.open("netslogo.jpg").resize((80, 80))
logo_img = ImageTk.PhotoImage(logo)

header = tk.Frame(root, bg="white")
header.pack(pady=10)

tk.Label(header, image=logo_img, bg="white").pack(side="left")
tk.Label(header, text="EETS Simulator NETS-AIIMS", font=("Arial", 26, "bold"), bg="white").pack(side="left", padx=10)

# -----------------------------
# TIMERS
# -----------------------------
timer_running = False
timer_value = 0

def update_timer():
    global timer_value
    if timer_running:
        timer_value += 1
        timer_box.config(text=str(timer_value))
    root.after(1000, update_timer)

def start_timer():
    print("Start Timer")
    global timer_running
    timer_running = True

def pause_timer():
    global timer_running
    timer_running = False
    

def stop_timer():
    global timer_running, timer_value
    timer_running = False
    timer_value = 0
    timer_box.config(text="0")

# -----------------------------
# CLOCK
# -----------------------------
def update_clock():
    now = datetime.now()
    date_value.config(text=now.strftime("%d-%m-%Y"))
    time_value.config(text=now.strftime("%H:%M:%S"))
    root.after(1000, update_clock)

# -----------------------------
# TOP BAR
# -----------------------------

datetime_frame = tk.Frame(root, bg="white")
datetime_frame.place(x=820, y=20)

tk.Label(datetime_frame, text="Date:", bg="white").grid(row=0, column=0)
date_value = tk.Label(datetime_frame, text="", bg="white", font=("Arial", 12, "bold"))
date_value.grid(row=0, column=1)

tk.Label(datetime_frame, text="Time:", bg="white").grid(row=1, column=0)
time_value = tk.Label(datetime_frame, text="", bg="white", font=("Arial", 12, "bold"))
time_value.grid(row=1, column=1)

update_clock()

# -----------------------------
# START BUTTON
# -----------------------------
start_btn = tk.Button(root, text="Start", font=("Arial", 18),
                      bg="#c69c6d", width=10, command=start_timer)
start_btn.pack(padx=20, pady=20)
start_btn.place(x=400, y=100)
# -----------------------------
# LEFT FRAME (Motor Controllers)
# -----------------------------
left_frame = tk.Frame(root, bg="#003153")
left_frame.place(x=10, y=150)

tk.Label(left_frame, text="Motor Controllers", font=("Arial", 18, "bold"),
         bg="#003153", fg="white").grid(row=0, column=0, columnspan=2, pady=10)

tk.Button(left_frame, text="Previous\nmodule", font=("Arial", 14), width=12,
          command=previous_module).grid(row=1, column=0, padx=10, pady=5)

tk.Button(left_frame, text="Next\nmodule", font=("Arial", 14), width=12,
          command=next_module).grid(row=1, column=1, padx=10, pady=5)

tk.Button(left_frame, text="-5", font=("Arial", 14), width=4,
          command=back15).grid(row=2, column=0, padx=10, pady=5)

tk.Button(left_frame, text="+5", font=("Arial", 14), width=4,
          command=next15).grid(row=2, column=1, padx=10, pady=5)

tk.Label(left_frame, text="Fine tune", font=("Arial", 14),
         bg="#003153", fg="white").grid(row=3, column=0, columnspan=2, pady=5)

tk.Button(left_frame, text="UP", font=("Arial", 14), width=10,
          command=up_module).grid(row=4, column=0, columnspan=2, pady=8)

tk.Label(left_frame, text="Plane", font=("Arial", 14),
         bg="#003153", fg="white").grid(row=5, column=0, columnspan=2, pady=5)

tk.Button(left_frame, text="DOWN", font=("Arial", 14), width=10,
          command=down_module).grid(row=6, column=0, columnspan=2, pady=8)

tk.Label(left_frame, text="Game Module", font=("Arial", 14),
         bg="#003153", fg="white").grid(row=6, column=2, columnspan=2, pady=5)
game_status = tk.Label(left_frame, text="Game 1", font=("Arial", 14),
                bg="#003153", fg="white")
game_status.grid(row=7, column=2, columnspan=2, pady=5)

# -----------------------------
# RIGHT FRAME (Timer, Snapshot)
# -----------------------------
right_frame = tk.Frame(root, bg="#003153")
right_frame.place(x=600, y=140)

tk.Label(right_frame, text="Timer (in sec):", font=("Arial", 16, "bold"),
         bg="#003153", fg="white").grid(row=0, column=0, pady=5)

timer_box = tk.Label(right_frame, text="0", font=("Arial", 18, "bold"),
                     width=6, bg="white")
timer_box.grid(row=0, column=1, padx=10)

tk.Label(right_frame, text="Snapshot", font=("Arial", 18, "bold"),
         fg="orange", bg="#003153").grid(row=1, column=0, pady=20)

tk.Button(right_frame, text="📸", font=("Arial", 20), width=3).grid(row=1, column=1)

tk.Label(right_frame, text="Recordings", font=("Arial", 18, "bold"),
         bg="#003153", fg="white").grid(row=2, column=0, columnspan=2, pady=20)

rec_frame = tk.Frame(right_frame, bg="#003153")
rec_frame.grid(row=3, column=0, columnspan=2)

tk.Button(rec_frame, text="Record", font=("Arial", 14), width=8,
          command=start_timer).grid(row=0, column=0, padx=5)

tk.Button(rec_frame, text="Pause", font=("Arial", 14), width=8,
          command=pause_timer).grid(row=0, column=1, padx=5)

tk.Button(rec_frame, text="Stop", font=("Arial", 14), width=8,
          command=stop_timer).grid(row=0, column=2, padx=5)


# Start timer loop
update_timer()

root.mainloop()

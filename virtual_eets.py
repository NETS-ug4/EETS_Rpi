import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("EETS Simulator")
root.geometry("950x550")
root.configure(bg="#1BF514")   # Blue background

# ==================================================
# TIMER VARIABLES
# ==================================================
timer_running = False
timer_value = 0

def update_timer():
    global timer_value
    if timer_running:
        timer_value += 1
        timer_box.config(text=str(timer_value))
    root.after(1000, update_timer)

# ==================================================
# CLOCK
# ==================================================
def update_clock():
    now = datetime.now()
    date_value.config(text=now.strftime("%d-%m-%Y"))
    time_value.config(text=now.strftime("%H:%M:%S"))
    root.after(1000, update_clock)

# ==================================================
# START / PAUSE / STOP
# ==================================================
def start_timer():
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

# ==================================================
# TOP BAR
# ==================================================
title = tk.Label(root, text="EETS Simulator", font=("Arial", 28, "bold"),
                 bg="#fcfcfc", fg="#000000")
title.pack(pady=10)

datetime_frame = tk.Frame(root, bg="#FFFFFF")
datetime_frame.place(x=770, y=20)

date_label = tk.Label(datetime_frame, text="Date:", font=("Arial", 12), bg="white")
date_label.grid(row=0, column=0, padx=5, pady=2)

date_value = tk.Label(datetime_frame, text="", font=("Arial", 12, "bold"), bg="white")
date_value.grid(row=0, column=1, padx=5)

time_label = tk.Label(datetime_frame, text="Time:", font=("Arial", 12), bg="white")
time_label.grid(row=1, column=0, padx=5, pady=2)

time_value = tk.Label(datetime_frame, text="", font=("Arial", 12, "bold"), bg="white")
time_value.grid(row=1, column=1, padx=5)

update_clock()   # Start real time clock

# ==================================================
# START BUTTON
# ==================================================
start_btn = tk.Button(root, text="Start", font=("Arial", 18),
                      bg="#c69c6d", width=10, command=start_timer)
start_btn.pack(pady=10)

# ==================================================
# LEFT PANEL – CONTROLLERS
# ==================================================
left_frame = tk.Frame(root, bg="#003153")
left_frame.place(x=40, y=140)

tk.Label(left_frame, text="Controllers", font=("Arial", 18, "bold"),
         bg="#003153", fg="white").grid(row=0, column=0, columnspan=3, pady=10)
tk.Button(left_frame, text="Previous\nmodule", font=("Arial", 14), width=12)\
    .grid(row=1, column=0, padx=10, pady=8)
tk.Button(left_frame, text="Next\nmodule", font=("Arial", 14), width=12)\
    .grid(row=1, column=1, padx=10, pady=8)

tk.Button(left_frame, text="-5", font=("Arial", 14), width=4)\
    .grid(row=2, column=0, padx=5, pady=8)
label = tk.Label(left_frame, text="Fine tune", font=("Arial", 14),
         bg="#003153", fg="white")
label.place(x=120, y=150)
tk.Button(left_frame, text="+5", font=("Arial", 14), width=4)\
    .grid(row=2, column=1, padx=5, pady=8)

tk.Button(left_frame, text="UP", font=("Arial", 14), width=10)\
    .grid(row=3, column=0, columnspan=3, pady=10)
tk.Label(left_frame, text="Plane", font=("Arial", 14),
         bg="#003153", fg="white").grid(row=4, column=0, columnspan=3)
tk.Button(left_frame, text="DOWN", font=("Arial", 14), width=10)\
    .grid(row=5, column=0, columnspan=3, pady=10)

# ==================================================
# RIGHT PANEL – TIMER, SNAPSHOT, RECORDING
# ==================================================
right_frame = tk.Frame(root, bg="#003153")
right_frame.place(x=600, y=140)

tk.Label(right_frame, text="Timer (in sec):", font=("Arial", 16, "bold"),
         bg="#003153", fg="white").grid(row=0, column=0, pady=5)

timer_box = tk.Label(right_frame, text="0", font=("Arial", 18, "bold"),
                     width=6, bg="white")
timer_box.grid(row=0, column=1, padx=10)

tk.Label(right_frame, text="Snapshot", font=("Arial", 18, "bold"),
         fg="orange", bg="#003153").grid(row=1, column=0, pady=20)
tk.Button(right_frame, text="📸", font=("Arial", 20), width=3)\
    .grid(row=1, column=1)

tk.Label(right_frame, text="Recordings", font=("Arial", 18, "bold"),
         bg="#003153", fg="white").grid(row=2, column=0, columnspan=2, pady=20)

rec_frame = tk.Frame(right_frame, bg="#003153")
rec_frame.grid(row=3, column=0, columnspan=2)

tk.Button(rec_frame, text="Record", font=("Arial", 14), width=8, command=start_timer)\
    .grid(row=0, column=0, padx=5)
tk.Button(rec_frame, text="Pause", font=("Arial", 14), width=8, command=pause_timer)\
    .grid(row=0, column=1, padx=5)
tk.Button(rec_frame, text="Stop", font=("Arial", 14), width=8, command=stop_timer)\
    .grid(row=0, column=2, padx=5)

# Start timer loop
update_timer()

root.mainloop()

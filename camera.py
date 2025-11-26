import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import cv2
import time

running = False
recording = False
cap = None
out = None
cam_window = None
cam_label = None

start_time = 0  # for recording timer


def open_camera_window():
    global cam_window, cam_label

    cam_window = Toplevel(root)
    cam_window.title("Camera Display")
    cam_window.geometry("700x550")

    cam_label = tk.Label(cam_window)
    cam_label.pack()

def start_camera():
    global running, cap

    if running:
        return

    running = True

    open_camera_window()

    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(3, 640)
    cap.set(4, 480)

    show_frame()


def stop_camera():
    global running, recording, cap, out

    running = False

    if recording:
        stop_recording()

    if cap:
        cap.release()

    if cam_window:
        cam_window.destroy()

    # Reset status indicators
    record_dot.config(text="●", fg="grey")
    record_timer.config(text="00:00:00")


def show_frame():
    global cap, running, recording, out, start_time

    if not running:
        return

    ret, frame = cap.read()
    if ret:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        cam_label.imgtk = imgtk
        cam_label.config(image=imgtk)

        # Save video frame
        if recording and out is not None:
            out.write(frame)

            # Update timer
            elapsed = int(time.time() - start_time)
            h = elapsed // 3600
            m = (elapsed % 3600) // 60
            s = elapsed % 60
            record_timer.config(text=f"{h:02}:{m:02}:{s:02}")

    cam_label.after(10, show_frame)


def start_recording():
    global recording, out, start_time

    if recording:
        return

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    filename = "rec_" + time.strftime("%Y%m%d_%H%M%S") + ".mp4"

    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
    recording = True
    start_time = time.time()

    record_dot.config(fg="green")  # GREEN DOT when recording
    print("Recording:", filename)


def stop_recording():
    global recording, out

    if not recording:
        return

    recording = False

    if out:
        out.release()
        out = None

    record_dot.config(fg="grey")
    record_timer.config(text="00:00:00")

    print("Recording stopped")


def take_snapshot():
    global cap

    ret, frame = cap.read()
    if ret:
        filename = "snap_" + time.strftime("%Y%m%d_%H%M%S") + ".jpg"
        cv2.imwrite(filename, frame)
        print("Snapshot saved:", filename)


# ------------------ MAIN WINDOW -------------------
root = tk.Tk()
root.title("RPi Camera Controller")
root.geometry("450x300")

# RECORDING STATUS AREA
status_frame = tk.Frame(root)
status_frame.pack(pady=10)

record_dot = tk.Label(status_frame, text="●", font=("Arial", 20), fg="grey")
record_dot.grid(row=0, column=0, padx=10)

record_timer = tk.Label(status_frame, text="00:00:00", font=("Arial", 20), fg="black")
record_timer.grid(row=0, column=1, padx=10)

# CAMERA CONTROL BUTTONS
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Start Camera", font=("Arial", 14),
          width=15, command=start_camera).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Stop Camera", font=("Arial", 14),
          width=15, command=stop_camera).grid(row=0, column=1, padx=10)

tk.Button(btn_frame, text="Start Recording", font=("Arial", 14),
          width=15, command=start_recording).grid(row=1, column=0, padx=10, pady=10)

tk.Button(btn_frame, text="Stop Recording", font=("Arial", 14),
          width=15, command=stop_recording).grid(row=1, column=1, padx=10, pady=10)

tk.Button(btn_frame, text="Snapshot", font=("Arial", 14),
          width=15, command=take_snapshot).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

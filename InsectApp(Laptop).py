import cv2
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk


class VideoApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.video_source = 0

        self.vid = cv2.VideoCapture(self.video_source)
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not self.vid.isOpened():
            print("Error: Could not open video device.")
        else:
            print("Capture device is open: " + str(self.vid.isOpened()))

        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        self.btn_start = Button(window, text="Start", width=10, command=self.start_video)
        self.btn_start.pack(anchor=tk.CENTER, expand=True)

        self.btn_stop = Button(window, text="Stop", width=10, command=self.stop_video)
        self.btn_stop.pack(anchor=tk.CENTER, expand=True)

        self.running = False
        self.delay = 15

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def start_video(self):
        print("Start button clicked")
        if not self.running:
            self.running = True
            self.update()

    def stop_video(self):
        print("Stop button clicked")
        self.running = False

    def update(self):
        if self.running:
            success, frame = self.vid.read()
            if success:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            else:
                print("No frame captured during the loop")
            self.window.after(self.delay, self.update)

    def on_closing(self):
        self.running = False
        self.vid.release()
        cv2.destroyAllWindows()
        self.window.destroy()


# 创建窗口并传递给 VideoApp 类
root = tk.Tk()
app = VideoApp(root, "Insects Application")

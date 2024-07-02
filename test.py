import cv2
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk

class VideoApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # 获取屏幕大小
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # 设置窗口大小为屏幕的一半，并居中显示
        window_width = screen_width // 2
        window_height = screen_height // 2
        self.window.geometry(f'{window_width}x{window_height}+{screen_width//4}+{screen_height//4}')

        self.video_source = 0
        
        self.vid = cv2.VideoCapture(self.video_source)
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
        
        if not self.vid.isOpened():
            print("Error: Could not open video device.")
        else:
            print("Capture device is open: " + str(self.vid.isOpened()))
        
        self.canvas = tk.Canvas(window, width=window_width, height=window_height - 50)
        self.canvas.pack()

        # Frame to hold buttons
        btn_frame = tk.Frame(window)
        btn_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.btn_start = Button(btn_frame, text="Start", width=10, command=self.start_video)
        self.btn_start.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_stop = Button(btn_frame, text="Stop", width=10, command=self.stop_video)
        self.btn_stop.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.running = False
        self.photo = None
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
        # 如果在树莓派上销毁窗口有问题，可以注释掉下面这一行
        cv2.destroyAllWindows()
        self.window.destroy()

# 创建窗口并传递给 VideoApp 类
root = tk.Tk()
app = VideoApp(root, "Insects Application")
 
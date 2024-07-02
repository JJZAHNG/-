import tkinter as tk
import picamera
import picamera.array
from PIL import Image, ImageTk
import os


class CameraApp:
    def __init__(self, master, camera_resolution=(640, 480)):
        self.master = master
        self.camera_resolution = camera_resolution

        # Add the path to libbcm_host.so
        os.environ['LD_LIBRARY_PATH'] = '/usr/lib/aarch64-linux-gnu/'

        print(os.environ['LD_LIBRARY_PATH'])

        # Initialize camera
        self.camera = picamera.PiCamera()
        self.camera.resolution = self.camera_resolution

        # Create a label to display the video feed
        self.label = tk.Label(master)
        self.label.pack()

        # Start capturing video
        self.capture_video()

    def capture_video(self):
        with picamera.array.PiRGBArray(self.camera) as stream:
            while True:
                self.camera.capture(stream, 'rgb', use_video_port=True)
                image = Image.fromarray(stream.array)
                photo = ImageTk.PhotoImage(image=image)
                self.label.config(image=photo)
                self.label.image = photo
                self.master.update()

                # Clear the stream in preparation for the next frame
                stream.seek(0)
                stream.truncate()


def main():
    root = tk.Tk()
    root.title("PiCamera Live Feed")

    # Adjust the window size and position as needed
    window_width = 800
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    app = CameraApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

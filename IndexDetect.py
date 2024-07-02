import cv2

# 尝试不同的设备索引
for index in range(5):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Device with index {index} opened successfully.")
        ret, frame = cap.read()
        if ret:
            print(f"Frame captured from device index {index}")
            cv2.imshow(f"Camera {index}", frame)
            cv2.waitKey(1000)  # 显示1秒
            cv2.destroyAllWindows()
        else:
            print(f"Failed to capture frame from device index {index}")
        cap.release()
    else:
        print(f"Could not open device with index {index}")

cv2.destroyAllWindows()

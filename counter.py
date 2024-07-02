import cv2
import numpy as np

def main():
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        # 读取帧
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # 将图像转换为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 使用高斯模糊减少噪声
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 应用二值化
        _, binary = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

        # 查找轮廓
        contours, _ = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 统计昆虫数量
        insect_count = 0
        for contour in contours:
            if cv2.contourArea(contour) < 100:
                continue
            insect_count += 1
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

        # 在图像上显示昆虫数量
        cv2.putText(frame, f'Insect Count: {insect_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # 显示结果
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

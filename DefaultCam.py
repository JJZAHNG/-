import cv2

videoIn = cv2.VideoCapture(0)
videoIn.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
videoIn.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not videoIn.isOpened():
    print("Error: Could not open video device.")
else:
    print("Capture device is open: " + str(videoIn.isOpened()))
    success, frame = videoIn.read()
    if not success:
        print("No frame captured initially")
    else:
        while success:
            cv2.imshow('Insects Camera', frame)
            success, frame = videoIn.read()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if not success:
            print('No frame captured during the loop')

videoIn.release()
cv2.destroyAllWindows()

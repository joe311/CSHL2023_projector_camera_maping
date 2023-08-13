import numpy as np
from matplotlib import pyplot as plt

import cv2 as cv


class CameraWrapper:

    def __init__(self, camera_num=1):
        self.cap = cv.VideoCapture(camera_num)

        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()
        ret, frame = self.cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")

        # prepare window
        self.fig1 = plt.figure()
        self.imshow = plt.imshow(np.zeros_like(frame))
        plt.ion()
        plt.show()

    def loop(self):
        print("Starting main loop")
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # update window
            self.imshow.set_data(frame)
            self.fig1.canvas.flush_events()

    def grabimage(self):
        ret, frame = self.cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            raise IOError("Can't read from camera")

        return frame

    def __del__(self):
        # When everything done, release the capture
        self.cap.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    cam = CameraWrapper(0)
    cam.loop()
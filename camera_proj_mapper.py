import numpy as np
from matplotlib import pyplot as plt

import cv2 as cv

cap = cv.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
ret, frame = cap.read()
if not ret:
    print("Can't receive frame (stream end?). Exiting ...")

# prepare window
fig1 = plt.figure()
imshow = plt.imshow(np.zeros_like(frame))
plt.ion()
plt.show()
while True:
    print("Starting main loop")
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # print(ret)

    # update window
    imshow.set_data(frame)
    fig1.canvas.flush_events()

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

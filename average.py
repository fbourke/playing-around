import cv2
import numpy as np
import random
import sys


video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()
dst = cv2.cv.fromarray(frame)

while True:
    # Capture frame-by-frame
    alpha = 0.96
    beta = 0.05
    ret, frame = video_capture.read()
    new_frame = cv2.cv.fromarray(frame)
    cv2.cv.AddWeighted(dst, alpha, new_frame, beta, 0, dst) 
    #cv2.cv.AddWeighted(dst, 0.5, new_frame, 0.5, 0, dst)  # for testing in live python

    # Display the resulting frame
    arr = np.asarray(dst)
    fl = cv2.flip(arr, 1)
    cv2.imshow('test', fl)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
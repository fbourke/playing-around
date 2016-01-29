import cv2
import numpy as np
import random
import sys

def logistic(x):
    exp_x = np.exp(x)
    return exp_x/(1+exp_x)

# initalise the camera
video_capture = cv2.VideoCapture(0)
# init our variables
ret, frame = video_capture.read()
dst = cv2.cv.fromarray(frame)
n = -1

while True:
    n = n+0.01
    alpha = logistic(n)
    beta = 1-alpha
    ret, frame = video_capture.read()
    # AddWeighted only takes cvmat type objects
    new_frame = cv2.cv.fromarray(frame)
    # the second to last parameter is gamma, which is added to the total (we don't need it)
    cv2.cv.AddWeighted(dst, alpha, new_frame, beta, 0, dst) 
    #cv2.cv.AddWeighted(dst, 0.5, new_frame, 0.5, 0, dst)  # for testing in live python

    # imshow only takes numpy arrays (this is stupid)
    arr = np.asarray(dst)
    # flip it so it's more natural to watch
    fl = cv2.flip(arr, 1)
    # put some instructions on screen
    cv2.putText(fl, 'Press r to reset', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2)
    # Display the resulting frame
    cv2.imshow('test', fl)

    if cv2.waitKey(1) & 0xFF == ord('r'):
        n = -1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
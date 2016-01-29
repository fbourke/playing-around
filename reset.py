import cv2
import numpy as np
import random
import sys
import time

def logistic(x):
    exp_x = np.exp(x)
    return exp_x/(1+exp_x)

# initalise the camera
video_capture = cv2.VideoCapture(0)
# init our variables
ret, frame = video_capture.read()
height, width, channels = frame.shape
dst = cv2.cv.fromarray(frame)
n = -1
start = time.time()

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
    color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
    cv2.putText(fl, 'Press r to reset', (width-550,height-25), cv2.FONT_HERSHEY_DUPLEX, 2, color, 2)
    looptime = 1/(time.time() - start)
    cv2.putText(fl, 'Framerate: %.3f FPS' % looptime, (10,height-25), cv2.FONT_HERSHEY_DUPLEX, 1, color, 2)
    # Display the resulting frame
    cv2.imshow('test', fl)
    start = time.time()

    if cv2.waitKey(1) & 0xFF == ord('r'):
        n = -1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
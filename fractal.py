import cv2
import numpy as np
import random
import sys

# generate blank image
width = 800
height = 600
image = blank_image = np.zeros((height,width,3), np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# make a center dot
cv2.circle(image, (width/2,height/2), 2, (0,255,0))

# make some lines
depth = 3
x = width/2
y = height/2
for d in range(1, depth):
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
	cv2.line(image, (x,y), (x+100/depth,y), color, thickness=1, lineType=8, shift=0)
	x = x+100/depth

# show the image
cv2.imshow("Fractal", image)
cv2.waitKey(0)

import cv2
import numpy as np
import random
import sys

def drawLines(start_x,start_y,depth): 
	if depth > 10:
		return
	x = start_x
	y = start_y
	d = depth
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
	cv2.line(image, (x,y), (x+length/d,y), color, thickness=2, lineType=8, shift=0)
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
	cv2.line(image, (x,y), (x+length/d,y+deflection/d), color, thickness=2, lineType=8, shift=0)
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
	cv2.line(image, (x,y), (x+length/d,y-deflection/d), color, thickness=2, lineType=8, shift=0)
	drawLines(x+length/d, y, d+1)
	drawLines(x+length/d, y+deflection/d, d+1)
	drawLines(x+length/d, y-deflection/d, d+1)



# generate blank image
width = 800
height = 600
image = blank_image = np.zeros((height,width,3), np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# make a center dot
x = 10
y = height/2
cv2.circle(image, (x,y), 2, (0,255,0))

# make some lines
depth = 1
length = 200
deflection = 50
drawLines(x,y,depth)


# show the image
cv2.imshow("Fractal", image)
cv2.waitKey(0)

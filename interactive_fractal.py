import cv2
import numpy as np
import random
import time
import sys

finish = False

def drawLines(start_x,start_y,depth): 
	max_depth = 5
	if depth > max_depth:
		return
	x = start_x
	y = start_y
	d = depth
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
	cv2.line(image, (x,y), (x+length/d,y), color, thickness=(max_depth-depth)/2, lineType=8, shift=0)
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
	cv2.line(image, (x,y), (x+length/d,y+deflection/d), color, thickness=(max_depth-depth)/2, lineType=8, shift=0)
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
	cv2.line(image, (x,y), (x+length/d,y-deflection/d), color, thickness=(max_depth-depth)/2, lineType=8, shift=0)
	drawLines(x+length/d, y, d+1)
	drawLines(x+length/d, y+deflection/d, d+1)
	drawLines(x+length/d, y-deflection/d, d+1)


def recursiveTree(start_x,start_y,theta,depth): 
	max_depth = 7
	if depth > max_depth:
		return
	x = start_x
	y = start_y
	d = depth
	global finish
	print finish
	(new_x, new_y) = drawPolarLine((x,y), length/d, theta)
	cv2.imshow("Fractal", image)
	if not finish:
		key = cv2.waitKey(0)
	else:
		key = 0
	offset = 0
	threshold = 0
	# move left
	if (key == ord('a')) and not finish:
		offset = -np.pi/8
	# move right
	if key == ord('d') and not finish:
		offset = np.pi/8
	# finish the tree
	if key == ord('f') and not finish:
		finish = True
		threshold = 0

	branches = 1
	total_angle = np.pi/3
	for i in range(1,branches+2):
		if random.randint(0,255) > threshold:
			recursiveTree(new_x, new_y, theta + (i-1)*total_angle/branches - total_angle/2 + offset, d+1)	

def drawPolarLine((start_x,start_y), r, theta):
	x_len = r*np.cos(theta)
	y_len = r*np.sin(theta)
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
	cv2.line(image, (start_x,start_y), (int(start_x+x_len), int(start_y+y_len)), color, thickness=2)
	return (int(start_x+x_len), int(start_y+y_len))

# generate blank image
width = 800
height = 600
image = blank_image = np.zeros((height,width,3), np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# make a starting dot
x = width/2
y = height-10
cv2.circle(image, (x,y), 2, (0,255,0))

# make some lines
# depth = 1

length = 200
start_theta = 3*np.pi/2

cv2.imshow('video', image)

recursiveTree(x, y, start_theta, 1)
time.sleep(1)

cv2.imshow('video', image)
cv2.waitKey(0)

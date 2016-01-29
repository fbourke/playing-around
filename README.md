Playing Around
==============

This is me playing around with stuff, right now OpenCV

## face_detect.py ##

This takes an image path as the first argument and the cascade file as the second arguement, and produces an image with green squares around the detected faces. It's example code from somewhere.

## webcam.py ##

This takes a stream from the webcam, detects faces, and draws a green box around the detected faces. It also randomly generates a color, and puts a circle around the face of the random color.

## average.py ##

This displays a moving average of the image from the webcam. In the file, two constants, *alpha* and *beta* set the weight of the average and new frames.

	alpha = 0.96
    beta = 0.05
    
When they add to other than 1, the exposure will be different from the output of the webcam. Any more than about 1.10 and the image will be quite bright. 

## light.mov ##

This is a movie of *average.py* in action.



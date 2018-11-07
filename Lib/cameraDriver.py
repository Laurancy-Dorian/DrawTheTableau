from time import *
from picamera import *

"""
Takes a picture form the camera and saves it in the current directory in a jpg format
prereq :	resX > 0, resY > 0
		 	resX <= 2592, resY <= 1944
param :		String	filename	The name of the file
			Int		resX 		The X resolution of the picture
			Int 	resY		The Y resolution of the picture
"""
def takePic (filename ='image', resX = 1024, resY = 768):
	camera = PiCamera()
	camera.resolution = (resX, resY)
	camera.start_preview()
	camera.capture(filename + '.jpg')

from time import *
from picamera import *
import numpy as np

"""
Takes a picture from the camera and saves it in the current directory in a jpg format
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

"""
Takes a videp from the camera and saves it in the current directory in a h264 format
prereq :	resX > 0, resY > 0
		 	resX <= 1360, resY <= 720
param :		String	filename	The name of the file
			Int		resX 		The X resolution of the picture
			Int 	resY		The Y resolution of the picture
"""
def takeVid(filename ='video', time = 60, resX = 1024, resY = 768):
	camera = picamera.PiCamera()
	camera.resolution = (resX, resY)
	camera.start_recording(filename + '.h264')
	camera.wait_recording(time)
	camera.stop_recording()



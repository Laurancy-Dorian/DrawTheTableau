from cameraDriver import *
from motionse
from datetime import *

"""
Scan with the motion sensor. while there is movement, nothing happens.
When movements stop, then it takes a picture with the camera.
"""
def takeAutomatedPictures () :
	mvt_detected = False
	mvt = False

	# Scan the movements. Does nothing while there is movements
	while (!mvt_detected or mvt):
		mvt = detection()
		if (mvt) :
			mvt_detected = True

	# The while loop ended, this means the user stopped writing in the blackboard. We take a picture
	time.sleep(2)

	file_name = 'img' + datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S") 
	takePic(file_name)




"""
Sends a picture to a divice via scp
https://github.com/jbardin/scp.py
param : String 	path 				The path of the picture
		String 	ip_adress 			The ip adress of the device to send to
		String 	path_destination	The path in the device where to put the file	
"""
def sendPicture (path, ip_adress, path_destination)





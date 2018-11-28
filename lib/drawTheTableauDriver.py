from cameraDriver import *
from motionsensorDriver import *
from drawTheTableauLib import *
import datetime as dt
import time as t

"""
Scan with the motion sensor. while there is movement, nothing happens.
When movements stop, then it takes a picture with the camera.
"""
def takeAutomatedPictures () :
	mvt_detected = 0
	mvt = False
	nb_verif = 0


	# Scan the movements. Does nothing while there is movements
	# Comme le capteur peut avoir des rates, nous verifions 3 fois d'affilees s'il n'y a pas de mouvements
	while (mvt_detected < 2 or mvt or nb_verif < 3):
		t.sleep(1)
		mvt = detection()

		if (mvt) :
			if mvt_detected < 2 :
				mvt_detected += 1
			nb_verif = 0
			printDTT ("Mouvement detecte ! (" + str(mvt_detected) + "/2)")
		elif mvt_detected == 2 :
			nb_verif = nb_verif +1
			printDTT ("Aucun mouvement (" + str(nb_verif) + "/3)")
		else :
			if mvt_detected <2 :
				mvt_detected = 0
			printDTT ("Il n'y a pas encore eu de mouvements")	

	printDTT ("Plus de mvt : Photo dans 5 sec")
	# The while loop ended, this means the user stopped writing in the blackboard. We take a picture
	
	t.sleep(5)

	takeAndSavePic()
	printDTT ("Photo prise");

	return 1

def takeAndSavePic() :
	file_name = 'img/img' + dt.datetime.now().strftime("%Y_%m_%d-%H%M%S") 
	takePic(file_name)



"""
Sends a picture to a divice via scp
https://github.com/jbardin/scp.py
param : String 	path 				The path of the picture
		String 	ip_adress 			The ip adress of the device to send to
		String 	path_destination	The path in the device where to put the file	
"""
#def sendPicture (path, ip_adress, path_destination)
 


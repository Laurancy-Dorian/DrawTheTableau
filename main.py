import re
from lib import cameraDriver as cam
from lib import motionsensorDriver as motion
from lib import drawTheTableauLib as dtlib
from lib import drawTheTableauDriver as dtdriver
from lib import lcdDriver as lcd
from lib import interfaceMobile as im
import datetime as dt
import time as t
import os

def get_ip() :
    ip = os.popen("ifconfig | grep -o -m1 \"adr:.* \"").read()
    ip = ip[4:]
    ip = ip.split(' ', 1)[0]
    return ip


if __name__ == "__main__":
    lcd.initLCD()
    dtlib.printDTT("DrawTheTableau")
    print ("\n")

    #Reccuperation et affichage de l'IP
    dtlib.printDTT(get_ip())	
    t.sleep(10)

    #continuer = dtlib.inputDTT ("Voulez-vous prendre une image instantanee ?", "Prendre image ?")
    continuer = im.boolattenteReponse ("Voulez-vous prendre une image instantanee ?")
  
    while continuer : 
	dtlib.printDTT("Prise de photo")
    	dtdriver.takeAndSavePic()
	dtlib.printDTT("Photo prise !")
	print ("\n")
	#continuer = dtlib.inputDTT ("Voulez-vous prendre une autre image instantanee ?", "Prendre image ?")
	continuer = im.boolattenteReponse ("Voulez-vous prendre une image instantanee ?")
	
	

    #continuer = dtlib.inputDTT ("Voulez-vous effectuer une prise auto des images ?", "Prise auto img ?")
    continuer = im.boolattenteReponse ("Voulez-vous effectuer une prise auto des images ?")
    while continuer :

        dtlib.printDTT ("DEBUT DE LA PRISE AUTO D\'IMAGE")
        dtdriver.takeAutomatedPictures();
        dtlib.printDTT ("FIN DE LA PRISE AUTO D\'IMAGE")
	print ("\n")

        #continuer = dtlib.inputDTT ("Voulez-vous continuer la prise auto des images ?", "Continuer prise auto img ?")
	continuer = im.boolattenteReponse ("Voulez-vous continuer la prise auto des images ?")

    #rep = dtlib.inputDTT ("Voulez-vous envoyer les images sur une machine distante ?", "Envoyer sur machine distante ?")
    #TODO
    lcd.shutDownLCD()
    im.shutdown()



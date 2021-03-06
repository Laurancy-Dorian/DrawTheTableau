import lcdDriver as lcd 
import time as t
import interfaceMobile as im

"""
Round a number up to the nearest multiple of another
param : Int 	nb 			the number to round up
		Int 	multiple	the multiple to round
"""
def roundToNearestMultiple(nb, multiple):
	return (nb + multiple) - ((nb + multiple) % multiple)
  

"""
Permet de poser une question a l'utilisateur qui repond par oui (Y) ou non (N)
Retourne la reponse sous la forme d'un booleen
Parameters :
	- msg String 	Le message a afficher
"""
def inputDTT (msg, msgcourt = "") :
	rep = ""
	while rep == "":
		printDTT (msg + " (Y/N) ", msgcourt + ":Y/N")
		rep = str(raw_input (""))
		if rep != "Y" and rep != "y" and rep != "N" and rep != "n" :
			printDTT ("Erreur : Veuillez repondre \'Y\' pour oui et \'N\' pour non", "ERREUR : Entrez Y (oui) ou N (non)")
			rep = "" 
	return rep == "Y" or rep == "y"

"""
Affiche un message dans la sortie courante et sur l'ecran lcd
Parameters :
	- msg 		Le message a afficher
	- msgcourt 	La version courte du message pour l'affichage sur le lcd(< 32 caracteres)
"""
def printDTT(msg, msgcourt = ""):
	if (msgcourt == "") :
		msgcourt = msg
	print (msg)
	lcd.setText(msgcourt)
	im.sendMessage(msg)
	t.sleep(0.1)
	

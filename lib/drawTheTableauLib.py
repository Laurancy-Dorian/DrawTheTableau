import lcdDriver as lcd 

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
def inputDTT (msg) :
	rep = ""
	while rep == "":
		printDTT (msg + " (Y/N) ")
		rep = str(raw_input (""))
		if rep != "Y" and rep != "N" :
			printDTT ("Erreur : Veuillez repondre \'Y\' pour oui et \'N\' pour non")
			rep = "" 
	return rep == "Y"

"""
Affiche un message dans la sortie courante et sur l'ecran lcd
"""
def printDTT(msg):
	print (msg)
	lcd.setText(msg)

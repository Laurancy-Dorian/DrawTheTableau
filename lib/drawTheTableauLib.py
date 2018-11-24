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
def inputDTT (msg)
	rep = ""
	while rep == "":
		rep = str(raw_input (msg + " (Y/N) "))
		if rep != "Y" and rep != "N" :
			print ("Erreur : Veuillez repondre \'Y\' pour oui et \'N\' pour non")
			rep = "" 
	return rep == "Y"

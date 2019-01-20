import time
import drawTheTableauLib as dt

def rcvMessage() :
  path = "/home/dodo/DrawTheTableau/appMobile/instruction"
  # Lecture du fichier
  fichier = open(path, "r")
  msg =  fichier.read()
  fichier.close()

  # On supprime le contenu du fichier
  fichier = open(path, "w")
  fichier.write("")
  fichier.close()

  return msg
  
  
def sendMessage(msg = "") :
  fichier = open("/home/dodo/DrawTheTableau/appMobile/info", "w")
  fichier.write(msg)
  fichier.close()
  

def attenteReponse(msg = "Reponse : ", repAttendues=["oui", "non"]) :
    reponse = ""
    
    # On envoie le message
    dt.printDTT(msg)
    
    # On recommence la boucle jusqu'a obtenir une reponse satisfaisante
    while reponse == "" :
        # Lit la reponse
        reponse = rcvMessage()
	
        # Verifie si la reponse est correcte
        rep_correcte = False

        if len(repAttendues) != 0 :
          for rep_attendue in repAttendues :
	    
            if reponse.lower() == rep_attendue.lower() :
              rep_correcte = True
              reponse = rep_attendue
	else :
	   rep_correcte = True
            
      # Si la reponse n'est pas correcte, on affiche un message et on reinitialise reponse
        if rep_correcte is False :
          reponse = ""
	
	time.sleep(0.5)

    return reponse
  

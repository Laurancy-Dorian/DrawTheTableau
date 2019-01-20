def rcvMessage() :
  fichier = open("/home/dodo/DrawTheTableau/appMobile/instruction", "r")
  msg =  fichier.read()
  fichier.close()
  return msg
  
  
def sendMessage(msg = "") :
  fichier = open("/home/dodo/DrawTheTableau/appMobile/info", "w")
  fichier.write("msg")
  fichier.close()
  

def attenteReponse(msg = "Reponse : ", repAttendues=["oui", "non"]) :
    reponse: String = ""
    
    # On envoie le message
    sendMessage(msg)
    
    # On recommence la boucle jusqu'a obtenir une reponse satisfaisante
    while reponse == "" :
        # Lit la reponse
        reponse = rcvMessage()

        # Verifie si la reponse est correcte
        rep_correcte = false

        if (len(repAttendues) != 0 :
          for rep_attendue in repAttendues 
            if reponse.lower() == rep_attendue.lower() :
              rep_correcte = true
              reponse = rep_attendue
            else :
              rep_correcte = true
            
      # Si la reponse n'est pas correcte, on affiche un message et on reinitialise reponse
        if rep_correcte == FALSE :
          reponse = ""

    return reponse
  
attenteReponse()

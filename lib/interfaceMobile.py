def rcvMessage() :
  fichier = open("/var/www/html/DrawTheTableau/instruction", "r")
  msg =  fichier.read()
  fichier.close()
  return msg
  
  
def sendMessage(msg = "") :
  fichier = open("data.txt", "w")
  fichier.write("msg")
  fichier.close()

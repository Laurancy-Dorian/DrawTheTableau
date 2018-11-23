# coding: utf-8
"""
Librairie de gestion d'un ecran LCD
"""

import smbus
import time

# write_byte_data(Adresse, registre de commande, Valeur)
# Ex : write_byte_data(0x3e, 0x80, 0x01) ==> Clear display

bus = smbus.SMBus(1)  # pour I2C-1 (0 pour I2C-0)

# Adresse pour les couleurs
DISPLAY_RGB_ADDR = 0x62

# Adresse pour le texte
DISPLAY_TEXT_ADDR = 0x3e

"""
Initialise le LCD
"""
def initLCD() :
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)

"""
Change la couleur de l'ecran
param : rouge	(int)	La couleur rouge
		vert	(int)	La couleur verte
		bleu	(int)	La couleur bleue
prereq : 0 <= rouge,vert,bleu <= 255 
		"""
def setRGB(rouge,vert,bleu):
	# rouge, vert et bleu sont les composantes de la couleur qu'on vous demande
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,rouge)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,vert)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,bleu)
	print("Couleur ecran changee")

"""
Envoie  a l'ecran une commande concerant l'affichage des caracteres
"""
def textCmd(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)

"""
Ecris le texte sur le LCD
param : 	texte (String)	Le texte a ecrire
prereq : 	len(texte) <= 32
"""
def setText(texte):
	textCmd(0x01)	# Clear display
	textCmd(0x0F)	# Display on, block cursor
	textCmd(0x38)	# 2 lines

	time.sleep(1)

	# pour un caractere c a afficher :
	for i in range(0, len (texte)):
		c = texte[i]

		if (c == '\n' or i == 16):
			textCmd(0xc0)	 # Passer a la ligne

		if (c == '\n') :
			i+=1
			c = texte[i]
		bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

	print ("texte ecrit")

"""
Change la couleur du fond du LCD
param : couleur (String) 	Le nom de la couleur
"""
def setColor(couleur):
	print "couleur changee"

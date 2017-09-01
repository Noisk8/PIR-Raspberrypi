import sys
import RPi.GPIO as GPIO 
import pygame
import time 
#seccion sensor setup sensor board 40, bcm 21
GPIO.setmode (GPIO.BCM) 
PIR_PIN=21
#GPIO.setwarnings (True)
GPIO.setup(PIR_PIN,GPIO.IN)

#seccion sonido
path="sonidos/" #path de los sonidos
sonidos=["prueba.wav"] #nombre y extension de los sonidos encerrados en comillas y separados en comas
orden=0
mi_sonido=path+sonidos[orden]
print ("cantidad sonidos:")
print (len(sonidos))

volumen=0.7  #volumen entre 0 y 1
pygame.mixer.init()

sonido= pygame.mixer.Sound (mi_sonido)
sonido.set_volume(volumen)
playing=False

try:
	while True:
#		print ("evaluando")
		if GPIO.input (PIR_PIN)==1:
			mi_sonido=path+sonidos[orden]
			sonido= pygame.mixer.Sound(mi_sonido)
			print "Playing sound:" + mi_sonido
			print GPIO.input(PIR_PIN)
			print "Movimiento detectado"
			time.sleep (1)
			if playing==False:
				print "playing sound"
				sonido.play()
				playing=True				
				time.sleep(2)
				print "Status of playing is"
				print pygame.mixer.get_busy()				
				
#		else :
#			print "no hay movimiento"
		time.sleep (1)
		if (playing==True) and (pygame.mixer.get_busy()==False):
			playing=False
			print "Playing false"
			orden+=1
			if orden>=len(sonidos):
				orden=0
except KeyboardInterrupt:
	print "quit"
	GPIO.cleanup()
	sys.exit()


#luego pueden comentar todos los print

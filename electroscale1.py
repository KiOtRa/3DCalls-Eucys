import matplotlib.pyplot as plt
import numpy as np
import math
from pyfirmata import Arduino, PWM
from time import sleep
from tkinter import *

#Interface
root = Tk()
root.wm_title("Expo-Sciences 2022")
intensity = IntVar(root, name = "intensityName")
intensity.set(0)
result = 0.0
#Pyfirmata
port = '/dev/cu.usbmodem14201'
board = Arduino(port)
pin = 9
sleep(0.5)
board.digital[pin].mode = PWM

def sendPwm(intensityNormal):
	global pin
	pwm = intensityNormal/256.0 #float entre 0 et 1
	print("Intensity pourcentage for the pin {}: {}".format(pin,pwm*100))
	board.digital[pin].write(pwm)
	sleep(0.005)

def refresher(intensityNormal):
	#Label
	spires,rayon,distance = 100,0.05,0.02
	global result 
	mu = math.pi *0.0000001*4
	a=((mu * intensityNormal)/(2*rayon))
	b= (rayon/math.sqrt((rayon*rayon)+(distance*distance)))**3
	result= spires*a*b
	magnfield.configure(text="Magnetic field 2cm up: {}T".format(result))
	#Pwm
	sendPwm(intensityNormal)

root.geometry("800x600")
root.configure(bg="white")
changvar = Scale(root,from_ =255,to =0,bg="gray",orient=VERTICAL,length = 400, sliderlength=80,label="Controle de l'intensité",variable=intensity)
changvar.place(x=50,y=50)
magnfield = Label(root,bg="gray",text="Magnetic field 2cm up: {}T".format(result))
magnfield.place(x=50,y=500)
intensity.trace("w",lambda *args: refresher(intensity.get()))

root.mainloop()
sendPwm(0)

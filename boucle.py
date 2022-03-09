import numpy as np
from math import *
from pyfirmata import Arduino, PWM
from time import sleep

#Pyfirmata
port = '/dev/cu.usbserial-1420'
board = Arduino(port)
pin1 = 9
pin2 = 10
pin3 = 11
sleep(0.5)
board.digital[pin1].mode = PWM
board.digital[pin2].mode = PWM
board.digital[pin3].mode = PWM
def sendPwm(pin,pwm): #float entre 0 et 1
    board.digital[pin].write(pwm)
    sleep(0.005)
    print("alors: {}".format(pwm))


#    
def start():
    global pin1
    global pin2
    global pin3
    i=0
    while True:
        sendPwm(pin1,abs(sin(i*0.01)))
        sendPwm(pin2,abs(sin(i*0.01-0.2)))
        sendPwm(pin3,abs(sin(i*0.01-0.4)))
        i = i+1
        print("Pourcentage de l'intensité pour les pins: {},{},{}".format(round(abs(sin(i*0.01))*100),round(abs(sin(i*0.01-0.2))*100),round(abs(sin(i*0.01-0.4)*100))))
        sleep(0.1)



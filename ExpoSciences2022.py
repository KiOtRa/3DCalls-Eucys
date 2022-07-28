# For 9 electromagnets--
# The script send the average "luminosity" of each ninth of the image to the corresponding
# microcontroller linked to an electromagnet. --> This allows us to control magnetic field
# intensity depending of an image. 
import cv2 as cv
import numpy as np
from pyfirmata import ArduinoMega, PWM
from time import sleep

vid = cv.VideoCapture(1)
#Pyfirmata
port = '/dev/cu.usbmodem14201'
board = ArduinoMega(port)
pins = [3, 4, 5, 6, 7, 8, 9, 10,11]

sleep(0.5)
for pin in pins:
    board.digital[pin].mode = PWM



def sendPwm(img): #used to send signals to the Arduino card
    global pins 
    board.digital[pins[0]].write(1-(img[0,0])/255.0)#up left
    board.digital[pins[1]].write(1-(img[0,1])/255.0)#up middle
    board.digital[pins[2]].write(1-(img[0,2])/255.0)#up right
    board.digital[pins[3]].write(1-(img[1,0])/255.0)#middle
    board.digital[pins[4]].write(1-(img[1,1])/255.0)
    board.digital[pins[5]].write(1-(img[1,2])/255.0)
    board.digital[pins[6]].write(1-(img[2,0])/255.0)#down
    board.digital[pins[7]].write(1-(img[2,1])/255.0)
    board.digital[pins[8]].write(1-(img[2,2])/255.0)
    


while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #gray = cv.medianBlur(gray,5)
        ret,img = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) #treshold
        imgResized = cv.resize(img,(3,3),interpolation = cv.INTER_AREA)
        sendPwm(imgResized)
        print(imgResized)
        cv.imshow('Camera with the algorithm', img)
        if cv.waitKey(1) & 0xFF == ord('q'): # "q" to quit
            break

# After the loop release the cap object
vid.release()
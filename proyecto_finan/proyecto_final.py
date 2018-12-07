import serial
import time
from tkinter import *
import tkinter



 
def led_on():
     arduinoData.write(b'1')
     print("Luz g")
 
 
def led_off():
     arduinoData.write(b'0')


led_control_window= Tk()
btn=Button(led_control_window,text="LUZ GARAGE ON",command=led_on)
btn1=Button(led_control_window,text="LUZ GARAGE OFF",command=led_off)
btn.pack()
btn1.pack()

def led1_on():
     arduinoData.write(b'2')
 
 
def led1_off():
     arduinoData.write(b'3')     
 

btn2=Button(led_control_window,text="LUZ COCINA ON",command=led1_on)
btn3=Button(led_control_window,text="LUZ COCINA OFF",command=led1_off)
btn2.pack()
btn3.pack()

def led2_on():
     arduinoData.write(b'4')
 
 
def led2_off():
     arduinoData.write(b'5')     
 

btn4=Button(led_control_window,text="LUZ SALA ON",command=led2_on)
btn5=Button(led_control_window,text="LUZ SALA OFF",command=led2_off)
btn4.pack()
btn5.pack()

def led3_on():
     arduinoData.write(b'6')
 
 
def led3_off():
     arduinoData.write(b'7')     
 

btn6=Button(led_control_window,text="LUZ HABITACION 1 ON ",command=led3_on)
btn7=Button(led_control_window,text="LUZ HABITACION 1 OFF",command=led3_off)
btn6.pack()
btn7.pack()


def led4_on():
     arduinoData.write(b'8')
 
 
def led4_off():
     arduinoData.write(b'9')     
 

btn8=Button(led_control_window,text="LUZ BAÑO ON ",command=led4_on)
btn9=Button(led_control_window,text="LUZ BAÑO OFF",command=led4_off)
btn8.pack()
btn9.pack()


def led5_on():
     arduinoData.write(b'a')
 
 
def led5_off():
     arduinoData.write(b'b')     
 

btn10=Button(led_control_window,text="LUZ LABADERO ON",command=led5_on)
btn11=Button(led_control_window,text="LUZ LABADERO OFF",command=led5_off)
btn10.pack()
btn11.pack()

def led6_on():
     arduinoData.write(b'c')
 
 
def led6_off():
     arduinoData.write(b'd')     
 

btn12=Button(led_control_window,text="LUZ HABITACION ON",command=led6_on)
btn13=Button(led_control_window,text="LUZ HABITACION OFF",command=led6_off)
btn12.pack()
btn13.pack()


def led7_on():
     arduinoData.write(b'e,1,2,4,6,8,a,c')
 
 
def led7_off():
     arduinoData.write(b'f,0,3,4,5,7,9,b,d')     
 

btn14=Button(led_control_window,text="LUZ TODO ON",command=led7_on)
btn15=Button(led_control_window,text="LUZ TODO OFF",command=led7_off)
btn14.pack()
btn15.pack()





arduinoData = serial.Serial('com4',9600)

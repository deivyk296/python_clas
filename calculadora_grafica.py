from tkinter import *
import tkinter

#****************************

#Crear ventana
root= tkinter.Tk()
root.geometry("400x400")#WExHE or ALxAN
root.title("MI CALCULADORA")
root.resizable(FALSE,FALSE)
root.configure(background="#FFFFFF")#color fondo



#*************************
def btnclick(valor):
    global operador
    operador=operador+str(valor)
    input_text.set(operador)
def clear():
    global operador
    operador=("")
    input_text.set(operador)
def operacion():
    global operador
    try:
        
        opera=str(eval(operador))
    except:
        clear()
        opera=("error")
    input_text.set(opera)
#######################################
input_text=StringVar()
operador=""
    
Display = Entry(root, font = ('times new roman', 20, 'bold'), width = 22, bd = 15, insertwidth = 4, bg = "#FDFEFE", justify = "right", textvariable = input_text).place(x=30,y=15)


Boton1 = Button(root, text = "1", width = 7 , height = 3,command=lambda:btnclick(1)).place(x=90,y=100)
Boton2 = Button(root, text = "2", width = 7 , height = 3,command=lambda:btnclick(2)).place(x=150,y=100)
Boton3 = Button(root, text = "3", width = 7 , height = 3,command=lambda:btnclick(3)).place(x=210,y=100)
Boton4 = Button(root, text = "4", width = 7 , height = 3,command=lambda:btnclick(4)).place(x=90,y=150)
Boton5 = Button(root, text = "5", width = 7 , height = 3,command=lambda:btnclick(5)).place(x=150,y=150)
Boton6 = Button(root, text = "6", width = 7 , height = 3,command=lambda:btnclick(6)).place(x=210,y=150)
Boton7 = Button(root, text = "7", width = 7 , height = 3,command=lambda:btnclick(7)).place(x=90,y=200)
Boton8 = Button(root, text = "8", width = 7 , height = 3,command=lambda:btnclick(8)).place(x=150,y=200)
Boton9 = Button(root, text = "9", width = 7 , height = 3,command=lambda:btnclick(9)).place(x=210,y=200)
Boton10 = Button(root, text = "0", width = 7 , height = 3,command=lambda:btnclick(0)).place(x=90,y=250)
Boton11 = Button(root, text = "+", width = 7 , height = 3,command=lambda:btnclick("+")).place(x=150,y=250)
Boton12 = Button(root, text = "-", width = 7 , height = 3,command=lambda:btnclick("-")).place(x=210,y=250)
Boton13 = Button(root, text = "*", width = 7 , height = 3,command=lambda:btnclick("*")).place(x=90,y=300)
Boton14 = Button(root, text = "=", width = 7 , height = 3,command=operacion).place(x=150,y=300)
Boton15 = Button(root, text = "/", width = 7 , height = 3,command=lambda:btnclick("/")).place(x=210,y=300)
Boton16 = Button(root, text = "C", width = 7 , height = 3,command=lambda:clear()).place(x=210,y=350)
#Abrir ventana para el programa
root.mainloop()

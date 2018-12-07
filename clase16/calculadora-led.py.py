#Importar librerias para GUI
from Tkinter import *
import Tkinter
####################### 
root = Tkinter.Tk()
root.geometry("280x430")
root.title("mi calculadora")
root.resizable(FALSE,FALSE)
root.configure(background="#17A589")
############################
def btnClick(valor):
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
            opera=("ERROR")
        input_text.set(opera)
    
############################
input_text=StringVar()
operador=""

display=Entry(root,font=('arial',20,'bold'),width=15,bd=20,insertwidth=10,bg="#A93226",justify="right",textvariable=input_text).place(x=9,y=60)
boton1=Button(root,text="+",width=7,height=3,command=lambda:btnClick("+")).place(x=190,y=180)
boton2=Button(root,text="-",width=7,height=3,command=lambda:btnClick("-")).place(x=190,y=240)
boton3=Button(root,text="*",width=7,height=3,command=lambda:btnClick("*")).place(x=190,y=300)
boton5=Button(root,text="/",width=7,height=3,command=lambda:btnClick("/")).place(x=190,y=360)
boton6=Button(root,text="C",width=7,height=3,command=lambda:clear()).place(x=10,y=360)
boton7=Button(root,text="0",width=7,height=3,command=lambda:btnClick(0)).place(x=70,y=360)
boton8=Button(root,text="1",width=7,height=3,command=lambda:btnClick(1)).place(x=10,y=180)
boton9=Button(root,text="2",width=7,height=3,command=lambda:btnClick(2)).place(x=70,y=180)
boton10=Button(root,text="3",width=7,height=3,command=lambda:btnClick(3)).place(x=130,y=180)
boton11=Button(root,text="4",width=7,height=3,command=lambda:btnClick(4)).place(x=10,y=240)
boton12=Button(root,text="5",width=7,height=3,command=lambda:btnClick(5)).place(x=70,y=240)
boton13=Button(root,text="6",width=7,height=3,command=lambda:btnClick(6)).place(x=130,y=240)
boton14=Button(root,text="7",width=7,height=3,command=lambda:btnClick(7)).place(x=10,y=300)
boton15=Button(root,text="8",width=7,height=3,command=lambda:btnClick(8)).place(x=70,y=300)
boton16=Button(root,text="9",width=7,height=3,command=lambda:btnClick(9)).place(x=130,y=300)

boton4=Button(root,text="=",width=7,height=3,command=operacion).place(x=130,y=360)


root.mainloop()

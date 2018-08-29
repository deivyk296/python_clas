#operaciones_aritmeticas
import os
os.system("cls")
n1 = 0
n2 = 0
opc = 0
resultado = 0
print("operaciones aritmeticas")
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
print(".:menu de operaciones.:")
print("1.sumar numeros")
print("2.restar numeros")
print("3.multiplicar numeros")
print("4.dividir numeros")
opc = int(input("digite la operacion a realizar:"))
if opc == 1 :
	resultado = num1 + num2
	print("el resultado de la operacion es: ",resultado)
elif opc == 2 :
	resultado = num1 - num2
	print("el resultado de la operacion es: ",resultado)
elif opc == 3 :
	resultado = num1 * num2
	print("el resultado de la operacion es: ",resultado)
elif opc == 4 :
	resultado = num1 / num2
	print("el resultado de la operacion es: ",resultado)
else :
	print("Ha digitado una opcion incorrecta !!!")

	
	
	
	
  	


		
	

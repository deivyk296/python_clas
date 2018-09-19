##KEVIN DAVID MOLINA ORDOÑEZ
##DANIEL FELIPEOBANDO LOPEZ

print("***********************************************")
print(".:: SELECCIONA EL PRODUCTO DE TU INTERES ::.")
print("***********************************************")

print("1. Credito de libranza")
print("2. Credito de vivienda preaprobado")
print("3. credito compra de cartera")
print("4. credito compra de cartera libraza")
print("5. credito de libre intervencion")
print("seleccione su opcion :")
opc=input()
opc=int(opc)

pres1=0
cuotas1=0
pres2=0
cuotas2=0
pres3=0
cuotas3=0


if (opc>5):
    print(" no es posible",opc, "esta opcion")
    
    
if (opc<-1):
    print("no se puede ",opc,"negatibo")
   
if (opc==1):
    print("***********************************************")
    print(".:: ingreso de datos generales ::.")
    print("***********************************************")
    print("monto de prestamo a solisitar")
    pres1=input()
    pres1=float(pres1)
    print("ingrese plazo en meses de las cuotas")
    cuotas1=input()
    cuotas1=float(cuotas1)
    print("año de nasimirnto")
    año1=input()
    año1=float(año1)

if (opc==2):
    print("***********************************************")
    print(".:: ingreso de datos generales ::.")
    print("***********************************************")
    print("monto de prestamo a solisitar")
    pres2=input()
    pres2=float(pres2)
    print("ingrese plazo en meses de las cuotas")
    cuotas2=input()
    cuotas2=float(cuotas2)
    print("año de nasimirnto")
    año2=input()
    año2=float(año2)
    
if (opc==3):
    print("***********************************************")
    print(".:: ingreso de datos generales ::.")
    print("***********************************************")
    print("monto de prestamo a solisitar")
    pres3=input()
    pres3=float(pres3)
    print("ingrese plazo en meses de las cuotas")
    cuotas3=input()
    cuotas3=float(cuotas3)
    print("año de nasimirnto")
    año3=input()
    año3=float(año3)
    
prestamo1=pres1/cuotas1    
print("las cuota a pagar es",prestamo1,"pesos mensula")
prestamo2=pres2/cuotas2    
print("las cuota a pagar es",prestamo2,"pesos mensula")
prestamo3=pres3/cuotas3    
print("las cuota a pagar es",prestamo3,"pesos mensula")
    
    
    


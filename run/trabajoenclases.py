# declaracion de variables
# nombre="Link"
# edad="64"
# ejemplo de concatenacion
# print("hola", nombre, "su edad es", edad)

#print("ingrese su nombre")
#nombre=input()
#print("ingrese su edad")
#edad=input()
#print("hola", nombre, "su edad es", edad)

#suma
#n1=int(input("ingrese un numero "))
#n2=int(input("ingrese un numero "))
#print(n1+n2)

#multiplicación
#n1=int(input("ingrese un numero "))
#n2=int(input("ingrese un numero "))
#print("la multiplicacion es", n1*n2)

#votos
#cant=int(input("ingrese cantidad de votantes"))
#josh=0
#erick=0
#for i in range (cant):
#    vot=int(input("ingrese su voto 1.josh 2.erick"))
#    if vot==1:
#        print("su voto es para josh")
#        josh=josh+1
#    else:
#        print("su voto es para erick") 
#        erick=erick+1
#print("los votos de josh son", josh)
#print("los votos de erick son", erick)
#if josh>erick:
#    print("ganó josh")
#else:
#    print("ganó erick")

#contador
# import time
# num=10
# while num >=0:
#     print(num)
#     time.sleep(1)
#     num=num-1

#clave con intento

#generar un numero aleatorio entre el 1-50

# import random 
# print(random.randint(1,50))

#clave con 3 intentos

intentos=3
clave=1234

resp=int(input("ingrese su clave: "))
while resp!=clave or intentos==0:
    if resp==clave:
       print("bienvenido al sistema!")
    elif intentos==intentos-1:
       print(f"clave incorrecta, le quedan {intentos} intentos")
       resp=int(input("ingrese nuevamente su clave: "))
    else:
       print("sistema bloqueado")
       break

    




# print("bievenido a sushi buena pinta")
# while True:
#     print("qué roll desea llevar?")
#     print("roll vegetta")
#     print("roll willy")
#     print("roll stax")
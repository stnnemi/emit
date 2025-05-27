#en este archivo puedo dejar la c*** si quiero, es para ir practicando:)

# clave=2420
# intentos=3
# c=int(input("ingrese su clave: "))
# while clave!=c or intentos==0:
#     intentos-=1
#     print(f"clave incorrecta, le quedan {intentos} intentos")
#     c=int(input("ingrese su clave nuevamente: "))
#     if intentos<=1:
#         break

#     print("bienvenido al sistema")
# if intentos!=0 and clave==c:
#     print("bienvenido al sistema")
# else:
#     print("sistema bloqueado")





# contraseña=7777
# intentos=5
# c=int(input("ingrese su contraseña: "))
# while c!=contraseña:
#      intentos-=1
#      print(f"contraseña incorrecta, le quedan {intentos} intentos")
#      c=int(input("ingrese nuevamente su contraseña: "))
#      if intentos<=1:
#          break
  
# if c==contraseña:
#      print("bienvenido al sistema")
# else:
#      print("sistema bloqueado")

#calculadora un intento

# num1=int(input("ingrese un número: "))
# num2=int(input("ingrese un número: "))
# resp=int(input("que operación desea realizar? 1.suma 2.resta 3.multiplicación 4.division 5.salir: "))
# if resp==1:
#     print("la suma de los números es: ",num1+num2)
# elif resp==2:
#     print("la resta de los números es: ",num1-num2)
# elif resp==3:
#     print("la multiplicacion de los números es: ",num1*num2)
# elif resp==4:
#     print("la división de los números es: ",num1/num2)
# else:
#     resp==5
#     print("cerrando calculadora")


# VOTATOON
# Designe 2 cantdidatos. Pregunte cuanto votantes son
# por cada votante , debe peguntar por quin votrá
# cuente la cantidad de votos y muestre los resultados
# definir quien ganó la votacion. Considere empate

# ted=0
# rai=0
# cant=int(input("cuántas personas votarán?: "))
# for i in range (cant):
#     voto=0
#     while voto!=1 and voto!=2:
#         print("1.ted 2.rai")
#         voto=int(input("ingrese su voto: "))
#         if voto==1:
#             ted+=1
#         elif voto==2:
#             rai+=1
#         else:
#             print("error, ingrese un voto valido")
# print("los votos de ted son", ted)
# print("los votos de rai son", rai)
# if ted>rai:
#     print("ganó ted")
# elif ted<rai:
#     print("ganó rai")
# else:
#     print("empate")


# Crear un cajero automatico
# Tener en cuenta cajas de billetes de 5000 , 10000 y 20000
# Cada caja tine 30 billetes. Verificar si el monto solicitado
# Esta disponible en el cajero.Verificar si el monto solicidado
# es posible por el multiplo de los billetes disponibles
# Al terminar cada transaccion, debe mostrar saldo Disponible
# Debe haber 3 usuarios cada uno son su saldo correspondiente
# Usar clave secreta para iniciar y segun la clave 
# asociar el saldo disponible

# user1=0 #clave 1111 
# user2=0 #clave 2222
# user3=0 #clave 3333
# saldo1=1000000
# saldo2=1000000
# saldo3=1000000
# bc=5000 #billete de 5.000
# bd=10000 #billete de 10.000
# bv=20000 #billete de 20.000
# caja1=30*5000
# caja2=30*10000
# caja3=30*20000
# tcajero=caja1+caja2+caja3

# resp=int(input("ingrese su clave "))
# if resp==1111:
#     print("bienvenido user1, su saldo es de:$",saldo1)
#     cant=int(input("cuánto dinero quiere sacar? "))
#     if cant<5000:
#       print("error, monto mínimo requerido $5.000")
#     elif cant>tcajero:
#       print("error, no tenemos ese total de dinero")
#     tcajero-=cant
#     saldo1-=cant
#     print("saldo disponible:$",saldo1)
    
# elif resp==2222:
#         print("bienvenido user2, su saldo es de:$",saldo2)
#         cant=int(input("cuánto dinero quiere sacar? "))
#         if cant<5000:
#           print("error, monto mínimo requerido $5.000")
#         elif cant>tcajero:
#           print("error, no tenemos ese total de dinero")
#         tcajero-=cant
#         saldo2-=cant
#         print("saldo disponible:$",saldo2)
# elif resp==3333:
#         print("bienvenido user3, su saldo es de:$",saldo3)
#         cant=int(input("cuánto dinero quiere sacar? "))
#         if cant<5000:
#           print("error, monto mínimo requerido $5.000")
#         elif cant>tcajero:
#           print("error, no tenemos ese total de dinero")
#         tcajero-=cant 
#         saldo3-=cant
#         print("saldo disponible:$",saldo3)


# STREET FIGTHER #

# Designe 2 peleadores solicitando sus nombres
# cada peleador tiene 50 HP, debe mostrar la 
# barra de energia. Las peleas son por turnos #print("[]"*20)
# cada turno el peleador ataca entre 3 y 15
# Existe posibilidad de ataque critico del 20% sera atk*2
# gana el que le quita todo el HP al rival

# import random
# import time
# print("ingrese los nombres de los peleadores")
# p1=input("peleador 1: ")
# p2=input("peleador 2: ")
# hp1=50
# hp2=50
# turno=0

# while hp1>0 and hp2>0:
#     if turno %2==0:
#         ataquen=(3,15)
#         ataquec=(1,5)
#         print ("turno de ",p1)
#         if ataquec==1:
#             ataquen=ataquen*2
#             print("ataque critico")
#             time.sleep(2)
#             print(f"{p1} ha hecho {ataquen} de daño")
#         hp2-=ataquen
#         time.sleep(2)
#         print(f"vida de {p2} es {hp2}")
#     else:
#         print("turno de ",p2)
#         if ataquec==1:
#             ataquen=(3,15)
#             ataquec=(1,5)
#             ataquen=ataquen*2
#             print("ataque critico")
#             time.sleep(2)
#             print(f"{p2} ha hecho {ataquen} de daño")
#         hp1-=ataquen
#         time.sleep(2)
#         print(f"vida de {p1} es {hp1}")
# if hp1>hp2:   
#     print("ha ganado",p1)
# else:
#     print("ha ganado",p2)
        


# print("ingrese los nombres de los peleadores")
# p1=input("peleador 1: ")
# p2=input("peleador 2: ")
# hp1=50
# hp2=50
# import random
# import time
# ataque=random.randint(3,15)
# ataquec=random.randint(1,5)
# turno=random.randint(1,2)

# while hp1>0 and hp2>0:
#     if turno %2==0:
#         print("turno de ",p1)
#         if ataquec==3:
#             ataque*2
#             print("ataque critico")
#         hp2-=ataque
#         time.sleep(1)
#         print("vida de",p2)
#         print("▄"*hp2)
#     else:
#         print("turno de ",p2)
#         if ataquec==3:
#             ataque*2
#             print("ataque critico")
#         hp1-=ataque
#         time.sleep(1)
#         print("vida de",p1)
#         print("▄"*hp1)
#     turno+=1
# if hp1>hp2:
#     print("ha ganado",p1)
# else:
#     print("ha ganado",p2)


#Prueba n*2
#ejercicio 1

# sdad1=350000
# sdae1=280000
# sdad2=250000
# sdae2=200000
# bono=60000
# edad=40000
# q=int(input("ingrese su quintil: "))
# if q==1 or q==2:
#     print(f"usted recibe un bono adicional de {bono}")
#     e=int(input("ingrese su condición laboral (1.-empleado 2.-desempleado): "))
#     if e==1:
#         total1=sdae1+bono
#         ed1=int(input("ingrese su edad: "))
#         if ed1>65:
#             print(f"por ser mayor de 65 años usted recibe ${edad} extra")
#             total3=total1+edad
#             print(f"el valor del subsidio de arriendo es ${total3}")
#     else:
#         total2=sdad1+bono
#         ed2=int(input("ingrese su edad: "))
#         if ed2>65:
#             print(f"por ser mayor de 65 años usted recibe ${edad} extra")
#             total4=total2+edad
#             print(f"el valor del subsidio de arriendo es ${total4}")
#         else:
#             print(f"el valor del subsidio de arriendo es ${total2}")
# else:
#     e=int(input("ingrese su condición laboral (1.-empleado 2.-desempleado): "))
#     if e==1:
#         print(f"el valor del subsidio de arriendo es ${sdae2}")
#     else:
#         print(f"el valor del subsidio de arriendo es ${sdad2}")
#     ed3=int(input("ingrese su edad: "))
#     if ed3>65:
#         print(f"por ser mayor de 65 años usted recibe ${edad} extra")
#     else:
#         print(f"por ser menor de 65 años no recibe dinero extra")


#ejercicio 2

# import random
# num1=int(input("ingrese un número entero: "))
# num2=int(input("ingrese un número entero mayor que el primer número: "))
# while num1>num2:
#     print("error, siga las instrucciones")
#     num2=int(input("ingrese un número entero mayor que el primer número: "))
# numadivinar=random.randint(num1,num2)

# intento=3
# resp=int(input(f"intenta adivinar el número entre {num1} y {num2}: "))
# for i in range(1,3):
#    while resp!=numadivinar or resp==0:
#      intento-=1
#      if numadivinar>resp:
#       print("el número es mayor")
#       resp=int(input(f"te quedan {intento} intentos, intenta adivinar el número: "))
#      elif numadivinar<resp:
#       print("el número es menor")
#       resp=int(input(f"te quedan {intento} intentos, intenta adivinar el número: "))
#      elif numadivinar==resp:
#       print("felicitaciones, pudiste adivinar")
#      break
# print("el número es", numadivinar)

while True:
    try:
        op=int(input('''
                    Seleccione una opción
                    1.-
                    2.-
                    3.-
                    '''))
        match op:
            case 1:
                print("1")
            case 2:
                print("2")
            case 3:
                print("saliendo")
                break
            case _:
                ("opción invalida")
    except Exception:
        print("solo números enteros")
        
    





        
      
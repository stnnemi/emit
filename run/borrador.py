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

# import random
# num1=int(input("ingrese un número entero: "))
# num2=int(input("ingrese un número entero mayor que el primer número: "))
# while num1>num2:
#  print("error, siga las instrucciones")
#  num2=int(input("ingrese un número entero mayor que el primer número: "))
# numadivinar=random.randint(num1,num2)
# intento=3
# resp=int(input(f"intenta adivinar el número entre {num1} y {num2}: "))
# for i in range(1,3):
#  while resp!=numadivinar or resp==0:
#   intento-=1
#   if numadivinar>resp: 
#    print("el número es mayor")
#    resp=int(input(f"te quedan {intento} intentos, intenta adivinar el número: "))
#   elif numadivinar<resp:
#    print("el número es menor")
#    resp=int(input(f"te quedan {intento} intentos, intenta adivinar el número: "))
#   elif numadivinar==resp:
#    print("felicitaciones, pudiste adivinar")
#   break
# print("el número es", numadivinar)

# sdad1=350000
# sdae1=280000
# sdad2=250000
# sdae2=200000
# bono=60000
# edad=40000
# q=int(input("ingrese su quintil: "))
# if q==1 or q==2:
#    print(f"usted recibe un bono adicional de {bono}")
#    e=int(input("ingrese su condición laboral (1.-empleado 2.-desempleado): "))
#    if e==1:
#       total1=sdae1+bono
#       ed1=int(input("ingrese su edad: "))
#       if ed1>65:
#          print(f"por ser mayor de 65 años usted recibe ${edad} extra")
#          total3=total1+edad
#          print(f"el valor del subsidio de arriendo es ${total3}")
#    else:
#       total2=sdad1+bono
#       ed2=int(input("ingrese su edad: "))
#       if ed2>65:
#           print(f"por ser mayor de 65 años usted recibe ${edad} extra")
#           total4=total2+edad
#           print(f"el valor del subsidio de arriendo es ${total4}")
#       else:
#          print(f"el valor del subsidio de arriendo es ${total2}")
# else:
#   e=int(input("ingrese su condición laboral (1.-empleado 2.-desempleado): "))
#   if e==1:
#      print(f"el valor del subsidio de arriendo es ${sdae2}")
#   else:
#      print(f"el valor del subsidio de arriendo es ${sdad2}")
#   ed3=int(input("ingrese su edad: "))
#   if ed3>65:
#        print(f"por ser mayor de 65 años usted recibe ${edad} extra")
#   else:
#        print(f"por ser menor de 65 años no recibe dinero extra")

# ## Domingo de pascua ####
# Preguntar la Cantidad de niños de niños que buscan huevitos de chocolates
# Cuando se termine la busqueda , preguntar cantos huevos encontró cada uno
# y clasificarlos de la siguiente forma
# Menos de una docena : NOOB
# Entre una docena a 24: Master
# 25 huevos o mas :Legend
# Mostrar resumen, y mostrar la mayor cantidad de huevitos encontrados por un solo niño

# noob=0
# master=0
# legend=0
# top=0
# import random

# cantniños=int(input("cuantos niños van a buscar huevitos: "))

# for c in range (cantniños):
#     canthuevos=random.randint(5,30)
#     if canthuevos>top:
#         top=canthuevos
#     if canthuevos<12:
#         noob+=1
#     elif canthuevos>=12 and canthuevos<=24:
#         master+=1
#     else:
#         canthuevos>=25
#         legend+=1

# print(f'''
#       la cantidad de noob es {noob}
#       la cantidad de master es {master}
#       la cantidad de legend es {legend}
#       la mayor cantidad de huevitos encontrados es {top}
#       ''')

# import random
# while True:
#     try: 
#         cant=int(input("cuántos niños van a buscar huevitos?: "))
#         noob=0
#         master=0
#         legend=0
#         top=0
#         for i in range (cant):
#             huevos=random.randint(5,30)
#             print(f"el niño {i+1} encontró {huevos} huevitos")
#             if huevos>top:
#                 top=huevos
#             if huevos<12:
#                 noob+=1
#             elif huevos>=12 and huevos<=24:
#                 master+=1
#             else:
#                 legend+=1
            
#         print (f'''
#             la cantidad de noob es {noob}
#             la cantidad de master es {master}
#             la cantidad de legend es {legend}
#             la mayor cantidad de huevos encontrada es {top}
#             ''')
#         break
#     except Exception:
#         print("ingrese solo números enteros") 

# total=0
# cantfrito=0
# cantfrio=0
# cantpromo=0
# cantjunaeb=0
# print("Bienvenido a Sushi Rock")
# while True:
#     try:
#         resp=int(input('''
#                        ¿Qué desea llevar? Seleccione su requerimiento solo con números enteros
#                        1.- Rolls frito $5.000
#                        2.- Rolls frío $5.000
#                        3.- Promo 50 piezas $10.000
#                        4.- Menú junaeb $4.000
#                        5.- Salir
#                        '''))
#         match resp:
#             case 1:
#                 print("has seleccionado Rolls frito")
#                 total+=5000
#                 cantfrito+=1
#             case 2:
#                 print("has seleccionado Rolls frío")
#                 total+=5000
#                 cantfrio+=1
#             case 3:
#                 print("has seleccionado Promo 50 piezas")
#                 total+=10000
#                 cantpromo+=1
#             case 4:
#                 print("has seleccionado Menú junaeb")
#                 total+=4000
#                 cantjunaeb+=1
#             case 5:
#                 print ("finalizando la compra")
#                 break
#     except Exception:
#         print ("error, ingrese su respuesta con números enteros")
        
# print(f'''
#       Su pedido sería:
#       {cantfrito} Rolls fritos
#       {cantfrio} Rolls fríos
#       {cantpromo} Promo 50 piezas
#       {cantjunaeb} Menú junaeb
#       El total de su pedido es de ${total}
#       ''')

# Crea un programa que permita al usuario seleccionar entre los siguientes sabores de bubble tea:

# Taro ($3.500)

# Matcha ($3.500)

# Mango ($3.000)

# Lichi ($3.000)

# Finalizar pedido

# Debes acumular el total y llevar la cuenta de cuántos bubble tea de cada tipo se pidieron. Al finalizar, muestra un resumen.

# total=0
# canttaro=0
# cantmatcha=0
# cantmango=0
# cantlichi=0

# print ("Bienvenido a Bubble Tea :3")
# while True:
#     try:
#         resp=int(input('''
#         ¿Qué desea llevar? Seleccione su requerimiento solo con números enteros
#         1.-Taro $3.500
#         2.-Matcha $3.500
#         3.-Mango 3.000
#         4.-Lichi 3.000
#         5.-Salir
#         '''))
#         match resp:
#             case 1:
#                 print ("has seleccionado un Bubble Tea Taro")
#                 total+=3500
#                 canttaro+=1
#             case 2:
#                 print("has seleccionado un Bubble Tea Matcha")
#                 total+=3500
#                 cantmatcha+=1
#             case 3:
#                 print("has seleccionado un Bubble Tea Mango")
#                 total+=3000
#                 cantmango+=1
#             case 4:
#                 print("has seleccionado un Bubble Tea Lichi")
#                 total+=3000
#                 cantlichi+=1
#             case 5:
#                 print("finalizando pedido")
#                 break
#             case _:
#                 print("opción inválida, intente nuevamente")           
#     except Exception:
#         print("error, ingrese solo números enteros")
        
# print(f'''
#       Su pedido sería:
#       {canttaro} Bubble Tea Taro 
#       {cantmatcha} Bubble Tea Matcha
#       {cantmango} Bubble Tea Mango
#       {cantlichi} Bubble Tea Lichi
#       ---------------------------------
#       El total de su pedido es ${total}
#       ''')

#  Ejercicio 2: Pizzería “PizzaManía”
# El usuario puede pedir pizzas con los siguientes ingredientes adicionales (cada uno suma $1.000):

# 1.- Pepperoni

# 2.- Queso extra

# 3.- Champiñones

# 4.- Aceitunas

# 5.-Terminar

# Cada pizza base cuesta $5.000. Permite armar varias pizzas, mostrando el costo de cada una al final, y luego el total.

# Sugerencia: Usa un bucle dentro de otro para armar cada pizza.


# Ejercicio 3: Cine
# Un programa para vender entradas al cine con este menú:

# 1.-Entrada general ($4.000)

# 2.-Entrada estudiante ($2.500)

# 3.-Combo palomitas + bebida ($3.000)

# 4.-Solo bebida ($1.000)

# 5.-Finalizar compra

# Lleva el conteo de cada ítem y muestra un resumen con el total
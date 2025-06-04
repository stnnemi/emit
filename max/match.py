#MATCH

#Ejercicio calculadora
# def suma():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     print("el resultado de la suma es: ", n1 + n2)
# def resta():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     print("el resultado de la resta es: ", n1 - n2)
# def multiplicación():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     print("el resultado de la multipliación es: ", n1 * n2)
# def división():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     print("el resultado de la división es: ", n1 / n2)
# def calculadora():
#     while True:
#         op=int(input('''seleccione su opción
#                     1.-suma
#                     2.-resta
#                     3.-multiplicación
#                     4.-división
#                     5.-salir
#                     '''))
#         match op:
#             case 1:
#                 print("suma")
#                 suma()
#             case 2:
#                 print("resta")
#                 resta()
#             case 3:
#                 print("multiplicación")
#                 multiplicación()
#             case 4:
#                 print("división")
#                 división()
#             case 5:
#                 print("saliendo")
#                 break
#             case _:
#                 print("opción incorrecta")
# calculadora()
#----------------------------------------------------------------------------------
#Ejercicio menú sushi
# total=0
# cantfrito=0
# cantfrio=0
# cantpromo=0
# cantjunaeb=0
# print("Bienvenido a Sushi Rock")
# while True:
#     try:
#         resp=int(input('''
#         ¿Qué desea llevar? Seleccione su requerimiento solo con números enteros
#         1.- Rolls frito $5.000
#         2.- Rolls frío $5.000
#         3.- Promo 50 piezas $10.000
#         4.- Menú junaeb $4.000
#         5.- Salir
#         '''))
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
#             case _:
#                 print("opción incorrecta, intente nuevamente")
#     except Exception:
#         print ("error, ingrese su respuesta con números enteros")
        
# print(f'''
#       Su pedido sería:
#       {cantfrito} Rolls fritos
#       {cantfrio} Rolls fríos
#       {cantpromo} Promo 50 piezas
#       {cantjunaeb} Menú junaeb
#       ------------------------------------
#       El total de su pedido es de ${total}
#       ''')
#----------------------------------------------------------------------------------
# Ejercicio 1: "Tienda bubble tea"
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
#----------------------------------------------------------------------------------
#  Ejercicio 2: Pizzería “PizzaManía”
# El usuario puede pedir pizzas con los siguientes ingredientes adicionales (cada uno suma $1.000):
# 1.- Pepperoni
# 2.- Queso extra
# 3.- Champiñones
# 4.- Aceitunas
# 5.-Terminar
# Cada pizza base cuesta $5.000. Permite armar varias pizzas, mostrando el costo de cada una al final, y luego el total.
# Sugerencia: Usa un bucle dentro de otro para armar cada pizza.
#----------------------------------------------------------------------------------
# Ejercicio 3: Cine
# Un programa para vender entradas al cine con este menú:
# 1.-Entrada general ($4.000)
# 2.-Entrada estudiante ($2.500)
# 3.-Combo palomitas + bebida ($3.000)
# 4.-Solo bebida ($1.000)
# 5.-Finalizar compra
# Lleva el conteo de cada ítem y muestra un resumen con el total
#----------------------------------------------------------------------------------
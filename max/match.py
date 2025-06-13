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
# while True:
#     cupon=input("tiene un cupon de si/no/salir: ") 
#     if cupon=="si":
#         respcupon=input("ingrese su cupón: ")
#         if respcupon=="soyotaku":
#             dcto=total*0.1
#             preciofinal=total-dcto
#             totaldcto=preciofinal-dcto
#             print(f'''
#                 Su pedido sería:
#                 {cantfrito} Rolls fritos
#                 {cantfrio} Rolls fríos
#                 {cantpromo} Promo 50 piezas
#                 {cantjunaeb} Menú junaeb
#                 ------------------------------------
#                 Subtotal: ${total}
#                 Descuento por código: ${totaldcto}
#                 TOTAL: ${preciofinal}
#                 ''')
#             break
#         else:
#             print("código no válido")
#     elif cupon=="no" or cupon=="salir":
#         print(f'''
#         ****************************** 
#         TOTAL PRODUCTOS:
#         ****************************** 
#         {cantfrito} Rolls fritos
#         {cantfrio} Rolls fríos
#         {cantpromo} Promo 50 piezas
#         {cantjunaeb} Menú junaeb
#         ****************************** 
#         El total de su pedido es de ${total}
#         ''')
#         break
#     else:
#         print("error, escriba una de las 3 opciones")

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

# print("Bienvenido a PizzaManía")
# #productos
# totalpepperoni=0
# totalqueso=0
# totalvegetariana=0
# totalcarne=0
# preciototal=0
# pizza=5000
# while True:
#     try:
#         resp=int(input('''
#             ¿Que pizza desea llevar?
#             1.- Pepperoni
#             2.- Queso
#             3.- Vegetariana
#             4.- Carne
#             5.- Salir
#             El precio de cada una es de $5.000
#             '''))
#         match resp:
#             case 1:
#                 print("ha seleccionado una pizza de pepperoni")
#                 totalpepperoni+=1
#                 preciototal+=pizza
#             case 2:
#                 print("ha seleccionado pizza de queso")
#                 totalqueso+=1
#                 preciototal+=pizza
#             case 3:
#                 print("ha seleccionado pizza vegetariana")
#                 totalvegetariana+=1
#                 preciototal+=pizza
#             case 4:
#                 print("ha seleccionado pizza de carne")
#                 totalcarne+=1
#                 preciototal+=pizza
#             case 5:
#                 print ("terminando pedido")
#                 break
#             case _:
#                 print("opción inválida, intente nuevamente")
#         respextra=(input("¿desea agregarle un extra a su pizza? si/no: "))
#         if respextra=="si":
#             while True:
#                 try:
#                     extras=int(input('''
#                             1.- pepperoni
#                             2.- queso extra
#                             3.- champiñones
#                             4.- aceitunas
#                             5.- finalizar extras
#                             cada extra tiene un costo de $1.000
#                             '''))
#                     match extras:
#                         case 1:
#                             print("ha seleccionado pepperoni extra")
#                             preciototal+=1000
#                         case 2:
#                             print("ha seleccionado queso extra")
#                             preciototal+=1000
#                         case 3:
#                             print("ha seleccionado champiñones extra")
#                             preciototal+=1000
#                         case 4:
#                             print("ha seleccionado aceitunas extra")
#                             preciototal+=1000
#                         case 5:
#                             print("finalizando extras")
#                             break
#                         case _:
#                             print("opción incorrecta, intente nuevamente")
#                 except Exception:
#                    print("error, ingrese solo números enteros")
#         elif respextra=="no":
#             print("sin extras, continuando con su pedido")
#         else:
#             print("resputa invalida, solo ingrese un si/no")
#     except Exception:
#         print("error, ingrese solo números enteros")
# print(f'''
#       su pedido sería:
#       {totalpepperoni} pizzas de pepperoni
#       {totalqueso} pizzas de queso
#       {totalvegetariana} pizzas vegetarianas
#       {totalcarne} pizzas de carne
#       ---------------------------------------
#       el total de su pedido sería ${preciototal}
#       ''')

#----------------------------------------------------------------------------------

# Ejercicio 3: Cine
# Un programa para vender entradas al cine con este menú:
# 1.-Entrada general ($4.000)
# 2.-Entrada estudiante ($2.500)
# 3.-Combo palomitas + bebida ($3.000)
# 4.-Solo bebida ($1.000)
# 5.-Finalizar compra
# Lleva el conteo de cada ítem y muestra un resumen con el total

# preciototal=0
# entradageneral=0
# entradaestudiante=0
# combo=0
# bebida=0
# print("Bienvenido a CinePlanet")
# while True:
#     try:
#         resp=int(input('''
# ¿Qué desea comprar
# 1.-entraga general $4.000
# 2.-entrada estudiante $2.500
# 3.-combo palomitas + bebida $3.000
# 4.-solo bebida $1.000
# 5.-finalizar compra
# '''))
#         match resp:
#             case 1:
#                 print("ha seleccionado entrada general")
#                 preciototal+=4000
#                 entradageneral+=1
#             case 2:
#                 print("ha seleccionado entrada estudiante")
#                 preciototal+=2500
#                 entradaestudiante+=1
#             case 3:
#                 print("ha seleccionado combo palomitas + bebida")
#                 preciototal+=3000
#                 combo+=1
#             case 4:
#                 print("ha seleccionado solo bebida")
#                 preciototal+=1000
#                 bebida+=1
#             case 5:
#                 print("finalizando compra")
#                 break
#             case _:
#                 print("opción inválida, intente nuevamente")
#     except Exception:
#         print("error, ingrese solo números enteros")
# print(f'''
# su pedido sería:
# {entradageneral} entrada(s) general
# {entradaestudiante} entrada(s) estudiante
# {combo} combo palomitas + bebida
# {bebida} bebida(s)
# --------------------------------------
# el total de su pedido sería ${preciototal}
# ''')  

#----------------------------------------------------------------------------------

# Bienvenido a la Heladería
# Menú:
# 1. Helado simple — $1.500
# 2. Helado doble — $2.500
# 3. Agregado de chocolate — $500
# 4. Agregado de manjar — $500
# 5. Finalizar compra
# El cliente puede comprar varios helados y agregarle chocolate o manjar.
# Al final, mostrar cuántos helados simples, dobles, chocolates y manjares compró,
# y el total a pagar.

# heladosimple = 0
# heladodoble = 0
# chocolate = 0
# manjar = 0
# preciototal = 0

# print("Bienvenido a la Heladería")

# while True:
#     try:
#         resp = int(input('''
# ¿Qué helado desea llevar?
# 1.- Helado simple $1.500
# 2.- Helado doble $2.500
# 3.- Finalizar compra
# '''))
#         match resp:
#             case 1:
#                 print("Ha seleccionado helado simple")
#                 heladosimple+=1
#                 preciototal+=1500
#                 respextra=input("¿Desea agregarle salsa extra? (si/no): ")
#                 if respextra=="si":
#                     while True:
#                         try:
#                             extra=int(input('''
# ¿Qué salsa desea agregar?
# 1.- Chocolate ($500)
# 2.- Manjar ($500)
# 3.- Terminar extras
# '''))
#                             match extra:
#                                 case 1:
#                                     print("Ha seleccionado salsa de chocolate")
#                                     chocolate+=1
#                                     preciototal+=500
#                                 case 2:
#                                     print("Ha seleccionado salsa de manjar")
#                                     manjar+=1
#                                     preciototal+=500
#                                 case 3:
#                                     print("Finalizando extras")
#                                     break
#                                 case _:
#                                     print("Opción inválida, intente nuevamente")
#                         except:
#                             print("Error, ingrese solo números enteros")
#                 elif respextra=="no":
#                     print("Continuando sin extras")
#                 else:
#                     print("Respuesta inválida, escriba si o no")

#             case 2:
#                 print("Ha seleccionado helado doble")
#                 heladodoble+=1
#                 preciototal+=2500
#                 respextra=input("¿Desea agregarle salsa extra? (si/no): ")
#                 if respextra=="si":
#                     while True:
#                         try:
#                             extra=int(input('''
# ¿Qué salsa desea agregar?
# 1.- Chocolate ($500)
# 2.- Manjar ($500)
# 3.- Terminar extras
# '''))
#                             match extra:
#                                 case 1:
#                                     print("Ha seleccionado salsa de chocolate")
#                                     chocolate+=1
#                                     preciototal+=500
#                                 case 2:
#                                     print("Ha seleccionado salsa de manjar")
#                                     manjar+=1
#                                     preciototal+=500
#                                 case 3:
#                                     print("Finalizando extras")
#                                     break
#                                 case _:
#                                     print("Opción inválida, intente nuevamente")
#                         except:
#                             print("Error, ingrese solo números enteros")
#                 elif respextra=="no":
#                     print("Continuando sin extras")
#                 else:
#                     print("Respuesta inválida, escriba si o no")

#             case 3:
#                 print("Finalizando compra")
#                 break
#             case _:
#                 print("Opción inválida, intente nuevamente")

#     except:
#         print("Error, ingrese solo números enteros")
# print(f'''
# Su pedido sería:
# {heladosimple} helado(s) simple
# {heladodoble} helado(s) doble
# {chocolate} agregado(s) de chocolate
# {manjar} agregado(s) de manjar
# -----------------------------
# El total de su pedido es de ${preciototal}
# ''')

#----------------------------------------------------------------------------------

# Bienvenido al Cine con Promoción
# Menú:
# 1. Entrada normal — $4.000
# 2. Entrada estudiante — $2.500
# 3. Combo (palomitas + bebida) — $3.000
# 4. Finalizar compra
# Si el cliente compra más de 3 entradas (normales + estudiantes),
# se aplica un 10% de descuento SOLO a las entradas.
# Al final, mostrar cuántas entradas normales, estudiantes y combos compró,
# y el total a pagar con descuento si corresponde.


#----------------------------------------------------------------------------------

# Bienvenido a la Librería
# Menú:
# 1. Libro de ficción — $10.000
# 2. Libro técnico — $12.000
# 3. Revista — $3.000
# 4. Bolígrafo — $1.000
# 5. Finalizar compra
# Si el cliente compra al menos UN libro (ficción o técnico) Y una revista,
# se aplica un 5% de descuento al total.
# Al final, mostrar cuántos de cada producto compró y el total con descuento si aplica.

#----------------------------------------------------------------------------------



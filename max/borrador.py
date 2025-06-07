#ejercicio huevitos
# ## Domingo de pascua ####
# Preguntar la Cantidad de niños de niños que buscan huevitos de chocolates
# Cuando se termine la busqueda , preguntar cantos huevos encontró cada uno
# y clasificarlos de la siguiente forma
# Menos de una docena : NOOB
# Entre una docena a 24: Master
# 25 huevos o mas :Legend
# Mostrar resumen, y mostrar la mayor cantidad de huevitos encontrados por un solo niño
# import random
# noob=0
# master=0
# legend=0
# top=0
# cantniños=int(input("cuántos niños van a buscar huevitos?: "))
# for i in range (cantniños):
#     while cantniños:
#         huevos=random.randint(5,30)
#         if huevos>top:
#             top=huevos
#         if huevos<12:
#             noob+=1
#         elif huevos>=12 and huevos<=24:
#             master+=1
#         else:
#             legend+=1
#         break
# print(f'''
#     hay un total de:
#     {noob} noob
#     {master} master
#     {legend} legend
#     y la mayor cantidad de huevitos encontrados fue de {top} huevos
#     ''') 




#ejercicio sushi

# total=0
# frito=0
# frio=0
# promo=0
# junaeb=0
# print("bienvenido a sushi rock")
# while True:
#     try:
#         resp=int(input('''
# ¿Qué desea llevar? Seleccione su requerimiento solo con números enteros
# 1.- Roll frito $5.000
# 2.- Roll frío $5.000
# 3.- Promo 50 piezas $10.000
# 4.- Menú junaeb $4.000
# 5.- Salir
# '''))
#         match resp:
#             case 1:
#                 print("has seleccionado roll frito")
#                 total+=5000
#                 frito+=1
#             case 2:
#                 print("has seleccionado roll frío")
#                 total+=5000
#                 frio+=1
#             case 3:
#                 print("has seleccionado promo 50 piezas")
#                 total+=10000
#                 promo+=1
#             case 4:
#                 print("has seleccionado menu junaeb")
#                 total+=4000
#                 junaeb+=1
#             case 5:
#                 print("terminando pedido")
#                 break
#             case _:
#                 print("opción inválida, intente nuevamente")
#     except Exception:
#         print("error, ingrese solo números enteros")
# while True:
#     respcupon=input("tiene un cupon de descuento? si/no/salir")
#     if respcupon=="si":
#         cupon=input("ingrese su cupon: ")
#         if cupon=="soyotaku":
#             print("")
# print(f'''
#       su pedido sería:
#       {frito} roll frito
#       {frio} roll frio
#       {promo} promo 50 piezas
#       {junaeb} menú junaeb
#       ------------------------
#       total: ${total}
#       ''')


 
# while True:
#     try:
#         empleadosrecientes=0
#         empleadosantiguos=0
#         cantempleados=int(input("ingrese la cantidad de empleados a registrar: "))
#         for i in range (cantempleados):
#             nombre=input("ingrese nombre del empleado: ")
#             while True:
#                 try:
#                     tiempo=int(input("ingrese años de antigüedad: "))
#                     if tiempo<=10:
#                         empleadosrecientes+=1
#                         print("10 o menos años de antigüedad")
#                         break
#                     else:
#                         empleadosantiguos+=1
#                         print("más de 10 años de antigüedad")
#                         break
#                 except Exception:
#                     print("debe ingresar un número entero")
#         break
#     except Exception:
#         print("error, ingrese un número entero")
# print(f'''
# Se registraron {empleadosantiguos} empleados con más de 10 años de antigüedad
# Se registraron {empleadosrecientes} empleados con 10 o menos años de antigüedad
#  ''')

#Ejercicio 2

# entradasdisponibles = 50
# while True:
#     try:
#         resp = int(input('''
#         *****Cine Estrella*****
#         Bienvenido al sistema de venta de entradas del Cine Estrella
#                     1.- Ver cuántas entradas quedan
#                     2.- Comprar una cantidad de entradas
#                     3.- Salir del sistema
#         '''))
#         match resp:
#             case 1:
#                 print(f"Entradas disponibles: {entradasdisponibles}")
#             case 2:
#                 while True:
#                     try:
#                         if entradasdisponibles>0:
#                             respentradas = int(input("¿Cuántas entradas desea comprar?: "))
#                             entradasdisponibles -= respentradas
#                             print(f"Compra exitosa. Quedan {entradasdisponibles} entradas")
#                             break
#                         else:
#                             print("Ya no quedan más entradas")
#                             break
#                     except Exception:
#                         print("Debe ingresar un número entero válido")
#             case 3:
#                 print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
#                 break
#             case _:
#                 print("Opción inválida. Por favor, selecciona una opción del 1 al 3")
#     except Exception:
#         print("Error, ingrese solo números enteros")
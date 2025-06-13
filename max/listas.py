# uso y ejemplos de listas
# que es una lista? 
# es una coleccion de datos

#     -5 -4  -3 -2 -1
# numeros=[7, 5, 33,24, 9]
#      0  1  2  3   4

# print(numeros[-1])

# for numero in numeros:
#     print("numero", numero*5)

# print(numeros)

# numeros.append(64)

# print(numeros)

# numeros.insert(3,100)

# print(numeros)

# frutas=["Manzana", "Mango", "Membrillo"]

# for fruta in frutas:
#     print(fruta)

#----------------------------------------------------------------------------------

# Shigeuru, Hideki, Hideo //lista de nombres
# Miyamoto, Anno, Kojima //lista apellidos

# Shigeru Miyamoto
# Hideki Anno
# Hideo Kojima

# nombres=[]
# apellidos=[]
# while True:
#     print('''
#         1.- Insertar Nombre y apellido
#         2.- Mostrar Nombres y apellidos
#         3.- Buscar nombre
#         4.-Salir
#           ''')
#     op=int(input("Seleccione una opcion: "))
#     match op:
#         case 1:
#             nom=input("Ingrese un nombre: ")
#             nombres.append(nom)
#             ape=input("Ingrese un nombre: ")
#             apellidos.append(ape)
#             print(apellidos)
#         case 2:
#             # c=0
#             # for n in nombres:
#             #     print(nombres[c], apellidos[c])
#             #     c+=1
#             for i in range(len(nombres)):
#                 print(nombres[i], apellidos[i])
#         case 3:
#             nom=input("Ingrese un nombre")
#             if nom in nombres:
#                 print(f"El nombre {nom} existe")
#             else:
#                 print(f"El nombre {nom} NO existe")
#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion Invalida")

#----------------------------------------------------------------------------------

# productos=["Disco SSD 1TB", "Memoria Ram 8GB", "Mouse"]
# precios=[70000, 30000, 15000]
# carrito=[]

# while True:
#     while True:
#         try:
#             print('''
#                 1.- Ingresar productos a la tienda
#                 2.- Comprar
#                 3.- Crear Boleta
#                 4.- Salir
#                 ''')
#             op=int(input("Ingese una opcion: "))
#             break
#         except Exception:
#              print("Ingrese un numero entero válido")
#     match op:
#         case 1:
#             pro=input("Ingrese el nombre del Producto: ")
#             productos.append(pro)
#             pre=int(input("Ingrese el Precio: "))
#             precios.append(pre)
#         case 2:
#                 for i in range(len(productos)):
#                     print(i+1, ".-", productos[i], "$", precios[i] )
#                 pro=int(input("Selecione que quiere comprar: "))
#                 carrito.append(pro-1)
#                 print(carrito)
#         case 3:
#             total=0
#             print("---------------0----------------")
#             print("Bienvenido a PC House ")
#             for i in carrito:
#                   print( productos[i], "----- $", precios[i] )
#                   total=total+precios[i]
#             print("Es total de articulos es", len(carrito))
#             print("Su total neto es ", total)
#             print("Su total mas iva es ", total*1.19)
#             print("---------------0----------------")

#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("opcion invalida")

#----------------------------------------------------------------------------------    

# Tarea
# Crear programa de manejo de notas
# 1.- Ingresar nota
# 2.- Borrar nota
# 3.- Mostar notas
# 4.- Sacar promedio, nota mayor y nota menor
# 5.- Limpiar todas las notas
# 6.- Salir


# notas=[7.0,4.6,4.9,7.0,5.6]

# while True:
#     while True:
#         try:
#             print('''   

#                 1.- ingresar notas
#                 2.- borrar nota
#                 3.- ver notas colocadas
#                 4.- promedio de notas, nota mayor y nota menor
#                 5.- borrar toda las notas
#                 6.- salir
#                     ''')
#             op=int(input())
#             break
#         except Exception:
#             print("Debe ingreser un numero entero valido")
    

#     match op:
#         case 1:
#             nota=float(input("ingrese la nota del alumno: "))
#             notas.append(nota)
#         case 2:
#             for num, n in enumerate(notas):
#                 print(num+1,".- ",n)
#             elim=int(input("ingrese cual quiere eliminar: "))
#             notas.pop(elim-1)
#         case 3:
#             print(notas)
#         case 4:
#             if len(notas) == 0:
#                 print("No hay notas para calcular el promedio.")
#             else:
#                 promedio=sum(notas)/len(notas)
#                 print(f"El promedio de las notas es: {round(promedio, 1)}")
#                 print("la nota mayor es", max(notas))
#                 print("la nota menor es", min(notas))
#         case 5:
#             notas.clear()
#         case 6:
#             print("saliendo...")
#             break
#         case _:
#             print("ya wey escoge algo valido")

#----------------------------------------------------------------------------------

# Tarea
# Crear programa de manejo de notas
# 1.- Ingresar nota
# 2.- Borrar nota
# 3.- Mostar notas
# 4.- Sacar promedio, nota mayor y nota menor
# 5.- Limpiar todas las notas
# 6.- Salir

# notas=[7.0,4.6,4.9,7.0,5.6]

# while True:
#     while True:
#         try:
#             resp=int(input('''
#             1.- ingresar notas
#             2.- borrar nota
#             3.- ver notas colocadas
#             4.- promedio de notas, nota mayor y nota menor
#             5.- borrar toda las notas
#             6.- salir
#                 '''))
#         except Exception:
#             print("ingrese un número entero válido")
    
#         match resp:
#             case 1:
#                 nota=float(input("ingrese su nota: "))
#                 notas.append(nota)
#             case 2:
#                 for i, nota in enumerate(notas):
#                     print(i+1, ".-", nota)
#                 sel=int(input("seleccione una nota a borrar: "))
#                 print("usted selecciono la nota ", notas[sel-1])
#                 notas.pop(sel-1)
#             case 3:
#                 print(notas)
#             case 4:
#                 promedio = sum(notas)/len(notas)
#                 print(f"su promedio es {promedio}")
#                 print(f"la nota mayor fue {max(notas)}")
#                 print(f"la nota menor fue {min(notas)}")
#             case 5:
#                 notas.clear()
#             case 6:
#                 print("saliendo")
#                 break
#             case _:
#                 print("error, ingresa una opción válida")

#----------------------------------------------------------------------------------


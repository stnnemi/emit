#explicacion y uso del match

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

#crear un menu de carrito con las siguientes opciones
#1.-ingresar nombre del usuario
#sera mostrada en la boleta, con un saludo



# def pan():
#     print("usted lleva un pan")
# def arroz():
#     print("usted lleva arroz")
# def leche():
#     print("usted lleva leche")
# def fideos():
#     print("usted lleva fideos")

# nom=input(f"ingrese su nombre ")
# total=0
# cant=0


# def carrito():
#     while True:
#         op=int(input('''seleccione su opción
#                     1.-pan $200
#                     2.-arroz $1.000
#                     3.-leche $1.000
#                     4.-fideos $800
#                     5.-salir
#                     '''))

#         match op:
#             case 1:
#                 print("pan")
#                 pan()
#                 pan+=200
#             case 2:
#                 print("arroz")
#                 arroz()
#                 arroz+=1000
#             case 3:
#                 print("leche")
#                 leche()
#                 leche+=1000
#             case 4:
#                 print("fideos")
#                 fideos()
#                 fideos+=800
#             case 5:
#                 print("saliendo")
#                 break
#             case _:
#                 print("opción incorrecta")
# carrito()

# cant=int(input("ingrese cantidad de alumnos: "))
# alumno=0
# alumno+=1
# cantnotas=int(input(f"ingrese cantidad de notas del alumno {alumno}: "))
# for i in range (cant):
#     while cant:
#         notas=int(input(f"ingrese su nota {nota}: "))
#         nota=0
#         nota+=1

# import random

# bala = random.randint(1,6)

# alumnos=int(input("Ingrese la cantidad de alumnos: "))

# prom=0
# contador=0

# for l in range (alumnos):
#     cantidadnotas=int(input(f"Ingrese su cantidad de notas del alumno {l+1} : "))
#     notas=0
#     for i in range (cantidadnotas):
#         nota=float(input(f"Ingrese la nota número {i+1} del alumno {l+1}: "))
#         notas+=nota
#     prom=notas/cantidadnotas
#     print(f"El promedio del alumno {l+1} es {prom}")
#     if prom>=4:
#         print(f"El alumno {l+1} ha aprobado")
#     else:
#         print(f"El alumno {l+1} ha reprobado")
#     contador+=prom
# promediogeneral=contador/alumnos
# print(f"El promedio general del curso es {promediogeneral}")
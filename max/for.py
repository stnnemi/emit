#pide un numero al usuario y muestra esa cant de repeticiones

# num=int(input("Ingrese un numero: ")) 
# for i in range(num):
#     print("Repeticion", i+1)
#-----------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
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
#-------------------------------------------------------------
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
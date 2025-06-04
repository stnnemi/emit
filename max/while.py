# clave=2420
# intentos=3
# c=int(input("ingrese su clave: "))
# while clave!=c or intentos==0:
#     intentos-=1
#     print(f"clave incorrecta, le quedan {intentos} intentos")
#     c=int(input("ingrese su clave nuevamente: "))
#     if intentos<=1:
#         break
# if intentos!=0 and clave==c:
#     print("bienvenido al sistema")
# else:
#     print("sistema bloqueado")
#----------------------------------------------------------------------------------
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
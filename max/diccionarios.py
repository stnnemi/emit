# dic={
#     "nombre":"Mel Broks",
#     "numero": 945453443,
#     "casado": True
# }

# # print(dic)

# for key,value in dic.items():
#     print(key,value)

# dic["ciudad"]="talca"

# for key,value in dic.items():
#     print(key,value)

# dic["casado"]=False

# for key,value in dic.items():
#     print(key,value)

# frutas={
#     "sandia":3000,
#     "manzana":1500,
#     "naranja":1000
# }

# print(frutas)
# fruta=input("ingrese una fruta: ")
# precio=int(input("ingrese precio: "))

# frutas[fruta]=precio

# print(frutas)

# usando diccionarios, haga este programa
# 1.-ingresar fruta y precio
# 2.-actualizar precio
# 3.-borrar fruta y precio
# 4.-mostrar todas las frutas y precios
# 5.-comprar
# 6.-salir

# while True:
#     try:
#         resp=int(input('''
#             1.-ingresar fruta y precio
#             2.-actualizar precio
#             3.-borrar fruta y precio
#             4.-mostrar todas las frutas y precios
#             5.-comprar
#             6.-salir
#                        '''))
#         match resp:
#             case 1:
#                 fruta=input("ingrese una fruta: ")
#                 precio=int(input("ingrese precio: "))
#             case 2:

#             case 3:
#                 for i, fruta in enumerate(frutas):
                    # print(i+1, ".-", fruta)
#                     sel=int(input("seleccione una fruta a borrar: "))
#                     print("usted selecciono la fruta ", frutas[sel-1])
#                     del frutas(sel-1)
#                     print(f"ahora el listado de frutas es {frutas}")
#             case 4:
#                 print(frutas)
#             case 5:
#                 comprar=input(f"¿qué fruta desea comprar?: {frutas}")
#             case 6:
#                 print("saliendo")
#                 break
#             case _:
#                 print("error, ingrese una opción válida")
#     except Exception:
#         print("error, ingrese un número entero")
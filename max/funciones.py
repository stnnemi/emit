# #funcion sin argumentos y sin return
# def suma():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     print(n1+n2)

# #funcoin sin argumentos y con return
# def suma_ret():
#     n1=int(input("ingrese un número: "))
#     n2=int(input("ingrese otro número: "))
#     return n1+n2

# #funcion con argumento y sin return
# def suma_arg(n1,n2):
#     print(n1+n2)

# #funcion con argumento y con return
# def suma_arg_ret(n1,n2):
#     return n1+n2
#----------------------------------------------------------------------------------
# #suma()
# #num=suma_ret()
# #print(num*5)
# num1=int(input("ingrese un número: "))
# num2=int(input("ingrese otro número: "))
# suma_arg(num1,num2)
# print("el resultado x 2 es",suma_arg_ret(num1,num2)*2)
#----------------------------------------------------------------------------------
# def cal_iva(n):
#     return n*0.19

# def cal_desc(precio, porc):
#     return precio*(porc/100)
#----------------------------------------------------------------------------------
# productos=[
#     {"nombre":"lapiz", "precio":400},
#     {"nombre":"goma", "precio":300},
#     {"nombre":"estuche", "precio":1600}

# ]

# print(productos)

# for item in productos:
#     print(f"el articulo {item["nombre"]} tiene un precio de {item["productos"]}")
#----------------------------------------------------------------------------------
#actividad
#1.-agregar articulo
#2.-borrar articulo
#3.-actualizar articulo
#4.-mostrar listado de articulos
#5.-salir

productos=[
    {"nombre":"lapiz", "precio":400},
    {"nombre":"goma", "precio":300},
    {"nombre":"estuche", "precio":1600}
]

# print(productos)

# for item in productos:
#     print(f"el articulo {item["nombre"]} tiene un precio de {item["productos"]}")

while True:
        resp=int(input('''
1.-agregar articulo
2.-borrar articulo
3.-actualizar articulo
4.-mostrar listado de articulos
5.-salir
                       '''))
        match resp:
            case 1:
                agregar=input("ingrese articulo para agregar: ")
                precio=int(input("ingrese el precio: "))
                productos.append({"agregar":agregar, "precio":precio})
            case 2:
                for i, producto in enumerate (productos):
                        print(i+1, ".-", producto)
                        borrar=input("ingrese un articulo a borrar: ")
                        productos.pop(borrar-1)
            case 3:
                actualizar=input("ingrese articulo a actualizar: ")
            case 4:
                for n, producto in enumerate(productos):
                    print(n+1, producto["nombre"], producto["precio"])
            case 5:
                print("saliendo...")
                break
            case _:
                print("error, ingrese una opción válida")
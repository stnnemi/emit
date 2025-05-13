#explicacion y uso del match

def suma():
    n1=int(input("ingrese un número: "))
    n2=int(input("ingrese otro número: "))
    print("el resultado de la suma es: ", n1 + n2)
def resta():
    n1=int(input("ingrese un número: "))
    n2=int(input("ingrese otro número: "))
    print("el resultado de la resta es: ", n1 - n2)
def multiplicación():
    n1=int(input("ingrese un número: "))
    n2=int(input("ingrese otro número: "))
    print("el resultado de la multipliación es: ", n1 * n2)
def división():
    n1=int(input("ingrese un número: "))
    n2=int(input("ingrese otro número: "))
    print("el resultado de la división es: ", n1 / n2)

def calculadora():
    while True:
        op=int(input('''seleccione su opción
                    1.-suma
                    2.-resta
                    3.-multiplicación
                    4.-división
                    5.-salir
                    '''))

        match op:
            case 1:
                print("suma")
                suma()
            case 2:
                print("resta")
                resta()
            case 3:
                print("multiplicación")
                multiplicación()
            case 4:
                print("división")
                división()
            case 5:
                print("saliendo")
                break
            case _:
                print("opción incorrecta")

calculadora()
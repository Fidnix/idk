import potencia

def inicio():
    operacion = input("Ingrese la operacion que desea realizar: ")

    if operacion == "P":
        p1 = input("Ingrese la base: ")
        p2 = input("Ingrese el exponente: ")
        potencia_r = potencia.MathMatics.potencia(p1, p2)

        print(f"El resultado es {potencia_r}")
    elif operacion == "F":
        p1 = int(input("Ingrese el numero para la factorial: "))
        factorial = potencia.MathMatics.factorial(p1= p1)

        print(f"El resultado es {factorial}")

if __name__ == '__main__':
    inicio()
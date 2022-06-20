import maths

def inicio():
    operacion = input("Ingrese la operacion que desea realizar: ")

    if operacion == "P":
        p1 = int(input("Ingrese la base: "))
        p2 = int(input("Ingrese el exponente: "))
        potencia = maths.MathMatics.maths(p1, p2)

        print(f"El resultado es {potencia}")
    elif operacion == "F":
        p1 = int(input("Ingrese el numero para la factorial: "))
        factorial = maths.MathMatics.factorial(p1= p1)

        print(f"El resultado es {factorial}")

    elif operacion == "Fi":
        p1 = int(input("Ingrese el numero de la serie que desea: "))
        fibo = maths.MathMatics.fibonacci(p1)

        print(f"EL resultado es {fibo}")

if __name__ == '__main__':
    print("Hola y bienvenido a este programa para hacer calculos hasicos")
    inicio()
class MathMatics:
    @staticmethod
    def potencia(p1,p2):
        return p1**p2

    @staticmethod
    def factorial( p1):
        if p1 == 1:
            return 1
        return p1*MathMatics.factorial(p1-1)

    @staticmethod
    def fibonacci(n):

        if n < 2:
            return 0
        elif n==2:
            return 1

        n1 = 1
        n2 = 1

        for i in range(1, n-1):
            n3 = n1+n2
            n1 = n2
            n2 = n3

        return n2
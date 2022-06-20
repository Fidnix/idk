class MathMatics:
    @staticmethod
    def potencia(p1,p2):
        return p1**p2

    @staticmethod
    def factorial( p1):
        if p1 == 1:
            return 1
        return p1*MathMatics.factorial(p1-1)
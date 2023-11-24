class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def semelhantes(self, triangulo):
        if ((self.a % triangulo.a) == 0) or ((triangulo.a % self.a) == 0):
            if ((self.b % triangulo.b) == 0) or ((triangulo.b % self.b) == 0):
                if ((self.c % triangulo.c) == 0) or ((triangulo.c % self.c) == 0):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
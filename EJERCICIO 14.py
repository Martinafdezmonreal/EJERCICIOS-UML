# Diagrama de objetos en código Python (Ejercicio 14)
# Supongamos que en el Ejercicio 13 se definieron las clases: Punto y poligono

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class triangulo:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

# Creamos los puntos
A = Punto(0, 0)
B = Punto(1, 0)
C = Punto(0, 1)
D = Punto(1, 1)

# Creamos dos triangulos con el lado AB en común
triangulo1 = triangulo(A, B, C)
triangulo2 = triangulo(A, B, D)

# Visualización sencilla de los objetos
print("Triángulo 1: ({}, {}), ({}, {}), ({}, {})".format(
    triangulo1.p1.x, triangulo1.p1.y,
    triangulo1.p2.x, triangulo1.p2.y,
    triangulo1.p3.x, triangulo1.p3.y
))
print("Triángulo 2: ({}, {}), ({}, {}), ({}, {})".format(
    triangulo2.p1.x, triangulo2.p1.y,
    triangulo2.p2.x, triangulo2.p2.y,
    triangulo2.p3.x, triangulo2.p3.y
))
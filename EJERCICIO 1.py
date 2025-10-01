# Definición de clases para cada figura geométrica

class Circulo:
    def __init__(self, color, diametro):
        self.color = color
        self.diametro = diametro

class Rectangulo:
    def __init__(self, color, longitud, anchura):
        self.color = color
        self.longitud = longitud
        self.anchura = anchura

class Cuadrado:
    def __init__(self, color, longitud):
        self.color = color
        self.longitud = longitud

class Elipse:
    def __init__(self, color, eje_mayor, eje_menor):
        self.color = color
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

# Creación de los objetos con los valores especificados

circulo_negro = Circulo(color="negro", diametro=1)
rectangulo_naranja = Rectangulo(color="naranja", longitud=3, anchura=1)
cuadrado_azul = Cuadrado(color="azul", longitud=1.5)
elipse_amarilla = Elipse(color="amarillo", eje_mayor=3, eje_menor=1)

# Mostrar los objetos creados
figuras = [circulo_negro, rectangulo_naranja, cuadrado_azul, elipse_amarilla]

for figura in figuras:
    print(vars(figura))
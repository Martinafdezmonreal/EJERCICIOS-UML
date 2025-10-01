# Ejercicio 15: Algoritmo para manejar puntos que pertenecen a varios polígonos

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.poligonos = []  # Lista de polígonos a los que pertenece este punto

    def agregar_poligono(self, poligono):
        if poligono not in self.poligonos:
            self.poligonos.append(poligono)

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

class Poligono:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = []  # Lista de puntos que forman el polígono

    def agregar_punto(self, punto):
        if punto not in self.puntos:
            self.puntos.append(punto)
            punto.agregar_poligono(self)

    def __repr__(self):
        return f"Poligono({self.nombre}, Puntos: {self.puntos})"

# Ejemplo de uso:
p1 = Punto(0, 0)
p2 = Punto(1, 0)
p3 = Punto(1, 1)
p4 = Punto(0, 1)

poligonoA = Poligono("A")
poligonoB = Poligono("B")

# p1 y p2 pertenecen a ambos polígonos
poligonoA.agregar_punto(p1)
poligonoA.agregar_punto(p2)
poligonoA.agregar_punto(p3)

poligonoB.agregar_punto(p1)
poligonoB.agregar_punto(p2)
poligonoB.agregar_punto(p4)

print(poligonoA)
print(poligonoB)
print(f"P1 pertenece a: {[p.nombre for p in p1.poligonos]}")
print(f"P2 pertenece a: {[p.nombre for p in p2.poligonos]}")
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"


class Poligono:
    def __init__(self, puntos: list[Punto]):
        if len(puntos) < 3:
            raise ValueError("Un polígono debe tener al menos 3 puntos.")
        self.puntos = puntos

    def __repr__(self):
        return f"Poligono({self.puntos})"

    def perimetro(self) -> float:
        perim = 0.0
        n = len(self.puntos)
        for i in range(n):
            p1 = self.puntos[i]
            p2 = self.puntos[(i + 1) % n]
            perim += ((p2.x - p1.x)**2 + (p2.y - p1.y)**2) ** 0.5
        return perim

    def area(self) -> float:
        n = len(self.puntos)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.puntos[i].x * self.puntos[j].y
            area -= self.puntos[j].x * self.puntos[i].y
        return abs(area) / 2


# Ejemplo: cuadrado de lado 1, vértices en (0,0), (1,0), (1,1), (0,1)
if __name__ == "__main__":
    cuadrado = Poligono([
        Punto(0, 0),
        Punto(1, 0),
        Punto(1, 1),
        Punto(0, 1)
    ])
    print("Cuadrado:", cuadrado)
    print("Perímetro:", cuadrado.perimetro())
    print("Área:", cuadrado.area())

    # Diagrama de clases (texto):

    # Clase Punto
    # - x: float
    # - y: float

    # Clase Poligono
    # - puntos: list[Punto]

    # Relación:
    # - Un Poligono tiene una lista de objetos Punto.
    # - Un Punto pertenece a un único Poligono (no se comparte entre polígonos).

    # Representación UML simplificada:
    #
    # +----------------+        1     *        +----------------+
    # |   Poligono     |---------------------->|     Punto      |
    # +----------------+                      +----------------+
    # | - puntos: list |                      | - x: float     |
    # +----------------+                      | - y: float     |
    #                                         +----------------+
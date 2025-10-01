from enum import Enum, auto

class Painting(Enum):
    MONALISA = auto()

class Person(Enum):
    MONA_LISA = auto()

class Painter(Enum):
    LEONARDO_DA_VINCI = auto()

class Location(Enum):
    LOUVRE_MUSEUM = auto()
    FRANCE = auto()
    ITALY = auto()

class Technique(Enum):
    OIL_PAINTING = auto()

class Material(Enum):
    POPLAR_WOOD = auto()

class ConservationStatus(Enum):
    EXCELLENT = auto()
    GOOD = auto()
    FAIR = auto()
    POOR = auto()

class Artwork:
    def __init__(self, cuadro, representa, pintor, lugar, copias, tecnica, material, ubicacion, conservacion):
        self.cuadro = cuadro
        self.representa = representa
        self.pintor = pintor
        self.lugar = lugar
        self.copias = copias
        self.tecnica = tecnica
        self.material = material
        self.ubicacion = ubicacion
        self.conservacion = conservacion

    def __str__(self):
        return (f"Cuadro: {self.cuadro.name}\n"
                f"Representa: {self.representa.name}\n"
                f"Pintor: {self.pintor.name}\n"
                f"Lugar de creación: {self.lugar.name}\n"
                f"¿Existen copias?: {'Sí' if self.copias else 'No'}\n"
                f"Técnica: {self.tecnica.name}\n"
                f"Material del soporte: {self.material.name}\n"
                f"Ubicación actual: {self.ubicacion.name}\n"
                f"Estado de conservación: {self.conservacion.name}")

# Ejemplo de uso
monalisa = Artwork(
    cuadro=Painting.MONALISA,
    representa=Person.MONA_LISA,
    pintor=Painter.LEONARDO_DA_VINCI,
    lugar=Location.ITALY,
    copias=True,
    tecnica=Technique.OIL_PAINTING,
    material=Material.POPLAR_WOOD,
    ubicacion=Location.LOUVRE_MUSEUM,
    conservacion=ConservationStatus.EXCELLENT
)

print(monalisa)
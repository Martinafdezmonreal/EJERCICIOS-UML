from enum import Enum
from typing import List

class Tecnica(Enum):
    OLEO = "Óleo"
    TEMPLE = "Temple"
    ACUARELA = "Acuarela"
    # Agrega más técnicas según sea necesario

class SubTecnica(Enum):
    VELADURA = "Veladura"
    IMPASTO = "Impasto"
    # Agrega más sub-técnicas según sea necesario

class Material(Enum):
    MADERA = "Madera"
    LIENZO = "Lienzo"
    CARTON = "Cartón"
    # Agrega más materiales según sea necesario

class EstadoConservacion(Enum):
    EXCELENTE = "Excelente"
    BUENO = "Bueno"
    REGULAR = "Regular"
    MALO = "Malo"

class Tiempo:
    def __init__(self, año: int, descripcion: str = ""):
        self.año = año
        self.descripcion = descripcion

class Texto:
    def __init__(self, contenido: str):
        self.contenido = contenido

class Cuadro:
    def __init__(
        self,
        titulos: List[Texto],
        cronologia: Tiempo,
        tecnica: Tecnica,
        subtecnica: SubTecnica,
        material: Material,
        autor: Texto,
        estado_conservacion: EstadoConservacion
    ):
        self.titulos = titulos  # 0..* Texto
        self.cronologia = cronologia  # 1 Tiempo
        self.tecnica = tecnica  # 1 enum Técnica
        self.subtecnica = subtecnica  # 1 enum Sub-Técnica
        self.material = material  # 1 enum Material
        self.autor = autor  # 1 Texto
        self.estado_conservacion = estado_conservacion  # 1 enum Estado de Conservación

# Ejemplo de uso:
if __name__ == "__main__":
    titulos = [Texto("La Gioconda"), Texto("Mona Lisa")]
    cronologia = Tiempo(1503, "Renacimiento")
    cuadro = Cuadro(
        titulos=titulos,
        cronologia=cronologia,
        tecnica=Tecnica.OLEO,
        subtecnica=SubTecnica.VELADURA,
        material=Material.MADERA,
        autor=Texto("Leonardo da Vinci"),
        estado_conservacion=EstadoConservacion.BUENO
    )
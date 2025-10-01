class ObraDeArte:
    def __init__(self, titulo, autor, cronologia, tecnica, subtecnica, soporte, descripcion, ubicacion, estado_conservacion):
        self.titulo = titulo
        self.autor = autor
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.estado_conservacion = estado_conservacion

class Museo:
    def __init__(self, nombre, ciudad, pais):
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.obras = []

    def agregar_obra(self, obra):
        self.obras.append(obra)

# Datos de la réplica
replica_gioconda = ObraDeArte(
    titulo="La Gioconda (Réplica)",
    autor="Anónimo (alumno de la escuela de Leonardo Da Vinci)",
    cronologia="1503 — 1516",
    tecnica="Óleo",
    subtecnica="Pincelada simple",
    soporte="Madera de nogal",
    descripcion=(
        "Réplica más antigua conocida de La Gioconda, procedente de las Colecciones Reales. "
        "Estudio del Museo del Prado concluye que fue realizada por un alumno de la escuela de Leonardo "
        "al mismo tiempo que el artista pintaba la original. Su estado de conservación es mejor que el de la obra original."
    ),
    ubicacion="Museo del Prado, Madrid",
    estado_conservacion="Muy bueno"
)

# Datos del museo
museo_prado = Museo(
    nombre="Museo del Prado",
    ciudad="Madrid",
    pais="España"
)

museo_prado.agregar_obra(replica_gioconda)

# Ejemplo de acceso a los datos
print(f"Obra: {replica_gioconda.titulo}")
print(f"Autor: {replica_gioconda.autor}")
print(f"Ubicación: {replica_gioconda.ubicacion}")
print(f"Estado de conservación: {replica_gioconda.estado_conservacion}")
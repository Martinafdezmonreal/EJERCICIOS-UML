# Algoritmo en Python que modela la descripción de la Catedral de Santiago de Compostela
# usando clases y objetos para representar el diagrama de objetos solicitado.

class Catedral:
    def __init__(self, nombre, ubicacion, provincia, comunidad, pais, inicio_construccion, materiales):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.provincia = provincia
        self.comunidad = comunidad
        self.pais = pais
        self.inicio_construccion = inicio_construccion
        self.materiales = materiales
        self.etapas_construccion = []
        self.estilos_arquitectonicos = []
        self.declaraciones = []

class EtapaConstruccion:
    def __init__(self, descripcion, fecha_inicio, fecha_fin=None):
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class EstiloArquitectonico:
    def __init__(self, nombre):
        self.nombre = nombre

class Declaracion:
    def __init__(self, tipo, fecha):
        self.tipo = tipo
        self.fecha = fecha

# Crear objeto principal
catedral = Catedral(
    nombre="Catedral de Santiago de Compostela",
    ubicacion="Santiago de Compostela",
    provincia="La Coruña",
    comunidad="Galicia",
    pais="España",
    inicio_construccion=1075,
    materiales=["granito"]
)

# Añadir etapas de construcción
catedral.etapas_construccion.append(EtapaConstruccion("Construcción inicial", 1075, 1122))
catedral.etapas_construccion.append(EtapaConstruccion("Consagración inicial", 1128))
catedral.etapas_construccion.append(EtapaConstruccion("Última etapa de construcción", 1168, 1211))
catedral.etapas_construccion.append(EtapaConstruccion("Consagración definitiva", "3 de abril de 1211"))

# Añadir estilos arquitectónicos
for estilo in ["románico", "gótico", "barroco", "plateresco", "neoclásico"]:
    catedral.estilos_arquitectonicos.append(EstiloArquitectonico(estilo))

# Añadir declaración de Bien de Interés Cultural
catedral.declaraciones.append(Declaracion("Bien de Interés Cultural", 1896))

# Ejemplo de visualización del diagrama de objetos (texto)
def mostrar_diagrama_objetos(catedral):
    print(f"Catedral: {catedral.nombre}")
    print(f"Ubicación: {catedral.ubicacion}, {catedral.provincia}, {catedral.comunidad}, {catedral.pais}")
    print(f"Materiales: {', '.join(catedral.materiales)}")
    print("Etapas de construcción:")
    for etapa in catedral.etapas_construccion:
        print(f"  - {etapa.descripcion}: {etapa.fecha_inicio} - {etapa.fecha_fin if etapa.fecha_fin else ''}")
    print("Estilos arquitectónicos:")
    for estilo in catedral.estilos_arquitectonicos:
        print(f"  - {estilo.nombre}")
    print("Declaraciones:")
    for declaracion in catedral.declaraciones:
        print(f"  - {declaracion.tipo} ({declaracion.fecha})")

# Mostrar el diagrama de objetos
mostrar_diagrama_objetos(catedral)
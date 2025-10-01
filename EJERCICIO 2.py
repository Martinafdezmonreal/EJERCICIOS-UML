# Definición de clases para representar el diagrama de objetos

class Persona:
    def __init__(self, nombre, apellido, apellido_nacimiento=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_nacimiento = apellido_nacimiento
        self.pareja = None
        self.padre = None
        self.madre = None

    def set_pareja(self, pareja):
        self.pareja = pareja
        pareja.pareja = self

    def set_padres(self, padre, madre):
        self.padre = padre
        self.madre = madre

# Crear objetos según el enunciado

# Padres de Guillermo
carlos = Persona("Carlos", "Windsor")
diana = Persona("Diana", "de Gales", apellido_nacimiento="Spencer")

# Guillermo y Kate
guillermo = Persona("Guillermo", "Windsor")
kate = Persona("Kate", "Windsor", apellido_nacimiento="Middleton")

# Relaciones
guillermo.set_padres(carlos, diana)
guillermo.set_pareja(kate)

# Mostrar el diagrama de objetos en texto
def mostrar_persona(persona):
    print(f"Nombre: {persona.nombre} {persona.apellido}", end="")
    if persona.apellido_nacimiento:
        print(f" (nacida {persona.apellido_nacimiento})", end="")
    print()
    if persona.pareja:
        print(f"  Pareja: {persona.pareja.nombre} {persona.pareja.apellido}")
    if persona.padre:
        print(f"  Padre: {persona.padre.nombre} {persona.padre.apellido}")
    if persona.madre:
        print(f"  Madre: {persona.madre.nombre} {persona.madre.apellido}", end="")
        if persona.madre.apellido_nacimiento:
            print(f" (nacida {persona.madre.apellido_nacimiento})", end="")
        print()
    print()

# Mostrar los objetos principales
mostrar_persona(guillermo)
mostrar_persona(kate)
mostrar_persona(carlos)
mostrar_persona(diana)
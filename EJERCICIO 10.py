class Proyecto:
    def __init__(self, nombre, tipo, duracion_meses):
        self.nombre = nombre
        self.tipo = tipo  # Ejemplo: 'Desarrollo de Software', 'Investigación', etc.
        self.duracion_meses = duracion_meses
        self.participantes = []

    def agregar_participante(self, persona):
        self.participantes.append(persona)
        persona.proyectos.append(self)

class Persona:
    def __init__(self, nombre, profesion, experiencia_anos):
        self.nombre = nombre
        self.profesion = profesion
        self.experiencia_anos = experiencia_anos
        self.proyectos = []

    def describir_experiencia(self):
        return f"{self.nombre} ({self.profesion}, {self.experiencia_anos} años de experiencia)"

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear personas
    ana = Persona("Ana", "Ingeniera de Software", 5)
    juan = Persona("Juan", "Analista de Datos", 3)

    # Crear proyectos
    proyecto1 = Proyecto("Sistema de Gestión", "Desarrollo de Software", 12)
    proyecto2 = Proyecto("Estudio de Mercado", "Investigación", 6)

    # Asociar personas a proyectos
    proyecto1.agregar_participante(ana)
    proyecto2.agregar_participante(juan)
    proyecto2.agregar_participante(ana)

    # Mostrar asociaciones
    for proyecto in [proyecto1, proyecto2]:
        print(f"Proyecto: {proyecto.nombre} ({proyecto.tipo})")
        print("Participantes:")
        for p in proyecto.participantes:
            print(" -", p.describir_experiencia())
        print()
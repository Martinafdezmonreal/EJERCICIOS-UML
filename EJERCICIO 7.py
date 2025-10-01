"""
Definición textual de las clases:

- Proyecto: Representa un proyecto profesional, con atributos como nombre, duración, tecnología utilizada y equipo.
- Equipo: Grupo de personas que trabajan en el proyecto, compuesto por profesionales de distintas áreas.
- Profesional: Persona que participa en el proyecto, con atributos como nombre, profesión y experiencia.
- Tecnologia: Herramienta, lenguaje o plataforma utilizada en el proyecto.

El modelo permite describir las características de los proyectos habituales, los profesionales involucrados y las tecnologías empleadas.
"""

class Tecnologia:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # Ejemplo: 'Lenguaje', 'Framework', 'Herramienta'

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Profesional:
    def __init__(self, nombre, profesion, experiencia_anos):
        self.nombre = nombre
        self.profesion = profesion
        self.experiencia_anos = experiencia_anos

    def __str__(self):
        return f"{self.nombre} - {self.profesion} ({self.experiencia_anos} años de experiencia)"

class Equipo:
    def __init__(self):
        self.miembros = []

    def agregar_profesional(self, profesional):
        self.miembros.append(profesional)

    def __str__(self):
        return "\n".join(str(miembro) for miembro in self.miembros)

class Proyecto:
    def __init__(self, nombre, duracion_meses, tecnologias, equipo):
        self.nombre = nombre
        self.duracion_meses = duracion_meses
        self.tecnologias = tecnologias  # Lista de objetos Tecnologia
        self.equipo = equipo            # Objeto Equipo

    def describir(self):
        print(f"Proyecto: {self.nombre}")
        print(f"Duración: {self.duracion_meses} meses")
        print("Tecnologías utilizadas:")
        for tech in self.tecnologias:
            print(f"  - {tech}")
        print("Equipo participante:")
        print(self.equipo)

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir tecnologías
    tech1 = Tecnologia("Python", "Lenguaje")
    tech2 = Tecnologia("Docker", "Herramienta")
    tech3 = Tecnologia("React", "Framework")

    # Definir profesionales
    prof1 = Profesional("Ana", "Desarrolladora Backend", 5)
    prof2 = Profesional("Luis", "DevOps", 3)
    prof3 = Profesional("Marta", "Desarrolladora Frontend", 4)

    # Definir equipo
    equipo = Equipo()
    equipo.agregar_profesional(prof1)
    equipo.agregar_profesional(prof2)
    equipo.agregar_profesional(prof3)

    # Definir proyecto
    proyecto = Proyecto(
        nombre="Sistema de Gestión Empresarial",
        duracion_meses=8,
        tecnologias=[tech1, tech2, tech3],
        equipo=equipo
    )

    # Describir proyecto
    proyecto.describir()
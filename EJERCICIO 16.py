from datetime import date

class Persona:
    def __init__(self, nombre, fecha_nacimiento, sexo):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento  # formato: YYYY-MM-DD
        self.sexo = sexo
        self.padres = []      # Cardinalidad: 0..2, rol: padre/madre
        self.hijos = []       # Cardinalidad: 0..*, rol: hijo/hija
        self.pareja = None    # Cardinalidad: 0..1, rol: pareja

    def agregar_padre(self, padre):
        if len(self.padres) < 2 and padre not in self.padres:
            self.padres.append(padre)
            padre.hijos.append(self)

    def agregar_hijo(self, hijo):
        if hijo not in self.hijos:
            self.hijos.append(hijo)
            hijo.padres.append(self)

    def establecer_pareja(self, pareja):
        self.pareja = pareja
        pareja.pareja = self

    def __str__(self):
        return f"{self.nombre} ({self.sexo}, nacido el {self.fecha_nacimiento})"

# Ejemplo de uso:
juan = Persona("Juan Pérez García", date(1990, 5, 15), "M")
maria = Persona("María García", date(1965, 8, 22), "F")
carlos = Persona("Carlos Pérez", date(1963, 3, 10), "M")

# Asociaciones familiares
juan.agregar_padre(maria)
juan.agregar_padre(carlos)
maria.establecer_pareja(carlos)

# Mostrar relaciones
print(f"Padres de {juan.nombre}: {[p.nombre for p in juan.padres]}")
print(f"Hijos de {maria.nombre}: {[h.nombre for h in maria.hijos]}")
print(f"Pareja de {maria.nombre}: {maria.pareja.nombre}")
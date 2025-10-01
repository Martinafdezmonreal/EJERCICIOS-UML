class Persona:
    def __init__(self, nombre, apellido1, apellido2, fecha_nacimiento, sexo, numero_identificacion):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento  # Formato: 'YYYY-MM-DD'
        self.sexo = sexo  # 'M' para masculino, 'F' para femenino, etc.
        self.numero_identificacion = numero_identificacion

    def __str__(self):
        return (f"Nombre: {self.nombre} {self.apellido1} {self.apellido2}\n"
                f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
                f"Sexo: {self.sexo}\n"
                f"Número de identificación: {self.numero_identificacion}")

# Ejemplo de uso
if __name__ == "__main__":
    persona = Persona(
        nombre="Juan",
        apellido1="Pérez",
        apellido2="García",
        fecha_nacimiento="1990-05-15",
        sexo="M",
        numero_identificacion="12345678A"
    )
    print(persona)
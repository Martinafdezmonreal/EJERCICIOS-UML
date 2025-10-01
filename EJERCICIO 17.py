from datetime import datetime, timedelta

class Libro:
    def __init__(self, id_libro, titulo, tematica, ejemplares=1):
        self.id_libro = id_libro
        self.titulo = titulo
        self.tematica = tematica
        self.ejemplares = ejemplares

class Prestamo:
    def __init__(self, libro, lector, fecha_prestamo, dias_maximos):
        self.libro = libro
        self.lector = lector
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_prestamo + timedelta(days=dias_maximos)
        self.devuelto = False

    def marcar_devuelto(self):
        self.devuelto = True

    def esta_atrasado(self, fecha_actual):
        return not self.devuelto and fecha_actual > self.fecha_entrega

class Lector:
    def __init__(self, id_lector, nombre, direccion):
        self.id_lector = id_lector
        self.nombre = nombre
        self.direccion = direccion
        self.penalizaciones = 0

    def aplicar_penalizacion(self):
        self.penalizaciones += 1

class Empleado(Lector):
    def __init__(self, id_empleado, nombre, direccion):
        super().__init__(id_empleado, nombre, direccion)
        self.es_empleado = True

class Estanteria:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.libros = []

    def agregar_libro(self, libro):
        if len(self.libros) < self.capacidad:
            self.libros.append(libro)
            return True
        return False

class Planta:
    def __init__(self, numero, estanterias):
        self.numero = numero
        self.estanterias = estanterias  # lista de Estanteria

    def capacidad_total(self):
        return sum(e.capacidad for e in self.estanterias)

class Biblioteca:
    def __init__(self, plantas):
        self.plantas = plantas  # lista de Planta
        self.libros = []
        self.lectores = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_lector(self, lector):
        self.lectores.append(lector)

    def realizar_prestamo(self, id_libro, id_lector, fecha_prestamo):
        libro = next((l for l in self.libros if l.id_libro == id_libro and l.ejemplares > 0), None)
        lector = next((lec for lec in self.lectores if lec.id_lector == id_lector), None)
        if libro and lector:
            dias_maximos = 60 if isinstance(lector, Empleado) else 30
            prestamo = Prestamo(libro, lector, fecha_prestamo, dias_maximos)
            self.prestamos.append(prestamo)
            libro.ejemplares -= 1
            return prestamo
        return None

    def devolver_libro(self, prestamo, fecha_devolucion):
        prestamo.marcar_devuelto()
        prestamo.libro.ejemplares += 1
        if fecha_devolucion > prestamo.fecha_entrega and not isinstance(prestamo.lector, Empleado):
            prestamo.lector.aplicar_penalizacion()
class EstructuraArqueologica:
    def __init__(self, codigo, datacion, materiales=None, estructuras=None):
        self.codigo = codigo  # Código identificador
        self.datacion = datacion  # Datación de la estructura
        self.materiales = materiales if materiales is not None else []  # Lista de materiales
        self.estructuras = estructuras if estructuras is not None else []  # Lista de otras estructuras (composición)

    def agregar_material(self, material):
        self.materiales.append(material)

    def agregar_estructura(self, estructura):
        if isinstance(estructura, EstructuraArqueologica):
            self.estructuras.append(estructura)

    def __str__(self):
        return (f"EstructuraArqueologica(codigo={self.codigo}, datacion={self.datacion}, "
                f"materiales={self.materiales}, estructuras={[e.codigo for e in self.estructuras]})")
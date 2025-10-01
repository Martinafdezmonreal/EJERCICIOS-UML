# Ejercicio 5: Definición de clases y atributos para figuras geométricas

class Figura:
    def __init__(self, color):
        self.color = color

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

class Cuadrado(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

class Elipse(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

# Ejemplo de instanciación de objetos
circulo1 = Circulo("negro", 1)
rectangulo1 = Rectangulo("naranja", 3, 1)
Cuadrado1 = Cuadrado("azul", 1.5)
Elipse1 = Elipse("amarillo", 1, 3)

# Mostrar atributos de los objetos
print(f"Circulo: color={circulo1.color}, radio={circulo1.radio}")
print(f"Rectangulo: color={rectangulo1.color}, base={rectangulo1.base}, altura={rectangulo1.altura}")
print(f"Cuadrado: color={Cuadrado1.color}, base={Cuadrado1.base}")
print(f"Elipse: color={Elipse1.color}, base={Elipse1.base}, altura={Elipse1.altura}")

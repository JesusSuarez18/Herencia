class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, color):
        self.color = color

    @property
    def ruedas(self):
        return self.ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self.ruedas = ruedas

    def __str__(self):
        return f'Color: {self.color} , Ruedas: {str(self.ruedas)}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    @property
    def velocidad(self):
        return self.velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self.velocidad = velocidad

    def __str__(self):
        return f'Coche: {super().__init__()}, Velocidad{self.velocidad}'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    @property
    def tipo(self):
        return self.tipo

    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta: {super().__init__()}, Tipo: {self.tipo}'

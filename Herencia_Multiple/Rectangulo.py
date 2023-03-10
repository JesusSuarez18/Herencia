from Figura_Geometrica import Figura_Geometrica
from Color import  Color

class Rectangulo(Figura_Geometrica,Color):
    def __init__(self,lado,color):
        Figura_Geometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def calcular_area(self):
        return self._ancho * self._alto

    def __str__(self):
        return f'{Figura_Geometrica.__str__(self)} {Color.__str__(self)}'
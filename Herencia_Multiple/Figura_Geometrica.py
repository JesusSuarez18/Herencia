from abc import ABC, abstractmethod


def _validar_valor(valor):
    return True if 0 < valor < 10 else False


class Figura_Geometrica(ABC):
    def __init__(self, ancho, alto):
        if _validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor fuera de rango: {ancho}')
        if _validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor fuera de rango: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if _validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor fuera de rango: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if _validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor fuera de rango: {alto}')

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'Ancho: {self._ancho}, Alto: {self._alto}'

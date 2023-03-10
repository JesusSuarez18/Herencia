from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5,'Verde')
print(f'Area: {cuadrado1.calcular_area()}')

#MRO --> Method Resolution Order
print(Cuadrado.mro())
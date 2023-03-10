from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

#MRO --> Method Resolution Order
print(Cuadrado.mro())

print('Cuadrado'.center(30,"-"))
cuadrado1 = Cuadrado(9, 'Azul')
print(cuadrado1)
print(f'Area del cuadrado: {cuadrado1.calcular_area()}')

print('Rectangulo'.center(30,"-"))
rectangulo1 = Rectangulo(9,4,'Verde')
print(rectangulo1)
print(f'Area del rectangulo: {rectangulo1.calcular_area()}')
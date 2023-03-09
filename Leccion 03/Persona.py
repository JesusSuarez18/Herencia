class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return f'Persona-> Nombre: {self.nombre}, Edad: {self.edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):  # Atributos de la clase "Persona"
        super().__init__(nombre, edad)  # Metodo super -> para poder acceder a los atributos de la clase Persona
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: {self.sueldo} {super().__str__()}'
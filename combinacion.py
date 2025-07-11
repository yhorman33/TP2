from abc import ABC, abstractmethod

class Estudiante(ABC):
    @abstractmethod
    def obtenerPromedio(self):
        pass

    @abstractmethod
    def mostrarInformacion(self):
        pass

class EstudianteDeGrado(Estudiante):
    def __init__(self, nombre, notas):
        self.__nombre = nombre
        self.__notas = notas

    def obtenerPromedio(self):
        return sum(self.__notas) / len(self.__notas)

    def mostrarInformacion(self):
        print(f"Estudiante de Grado: {self.__nombre}")
        print(f"Promedio: {self.obtenerPromedio():.2f}")

class EstudianteDePosgrado(Estudiante):
    def __init__(self, nombre, tesisCalificada):
        self.__nombre = nombre
        self.__tesisCalificada = tesisCalificada

    def obtenerPromedio(self):
        return 10.0 if self.__tesisCalificada else 0.0

    def mostrarInformacion(self):
        print(f"Estudiante de Posgrado: {self.__nombre}")
        estado = "Completada" if self.__tesisCalificada else "No completada"
        print(f"Tesis: {estado}, Promedio: {self.obtenerPromedio():.2f}")

# Lista de estudiantes
estudiantes = [
    EstudianteDeGrado("Lucía", [8.5, 9.0, 7.5]),
    EstudianteDePosgrado("Carlos", True),
    EstudianteDeGrado("Mateo", [6.0, 7.0, 8.0]),
    EstudianteDePosgrado("Ana", False)
]

for estudiante in estudiantes:
    estudiante.mostrarInformacion()
    print()

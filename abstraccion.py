from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def conducir(self):
        pass

class Coche(Vehiculo):
    def encender(self):
        print("Coche encendido.")

    def apagar(self):
        print("Coche apagado.")

    def conducir(self):
        print("Conduciendo coche por la ciudad.")

class Bicicleta(Vehiculo):
    def encender(self):
        print("La bicicleta no necesita encenderse.")

    def apagar(self):
        print("La bicicleta no necesita apagarse.")

    def conducir(self):
        print("Pedaleando bicicleta en el parque.")

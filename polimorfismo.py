class Empleado:
    def calcularSalario(self):
        return 0

class EmpleadoPorHora(Empleado):
    def __init__(self, horas, tarifa):
        self.horasTrabajadas = horas
        self.tarifaHora = tarifa

    def calcularSalario(self):
        return self.horasTrabajadas * self.tarifaHora

class EmpleadoFijo(Empleado):
    def __init__(self, salarioMensual):
        self.salarioMensual = salarioMensual

    def calcularSalario(self):
        return self.salarioMensual

# Lista de empleados
empleados = [
    EmpleadoPorHora(160, 5.5),
    EmpleadoFijo(1200),
    EmpleadoPorHora(100, 10)
]

for i, empleado in enumerate(empleados, 1):
    print(f"Empleado {i} - Salario: ${empleado.calcularSalario():.2f}")

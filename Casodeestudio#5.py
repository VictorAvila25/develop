class Empleado:
    def __init__(self, rol, nombre, cedula, balance):
        self.rol = rol
        self.nombre = nombre
        self.cedula = cedula
        self.balance = balance
    
    def retirar_dinero(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Saldo insuficiente para retirar el dinero.")
    
    def pagar_salario(self, salario):
        self.balance += salario

class Nomina:
    def __init__(self, presupuesto):
        self.presupuesto = presupuesto
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(f"Nombre: {empleado.nombre}, Rol: {empleado.rol}, Cédula: {empleado.cedula}")
    
    def pagar_nomina(self):
        total_salarios = 0
        for empleado in self.empleados:
            if empleado.rol == "Programador Junior":
                salario = 1000
            elif empleado.rol == "Programador Senior":
                salario = 2000
            elif empleado.rol == "Manager":
                salario = 3000
            else:
                salario = 0
            total_salarios += salario
            empleado.pagar_salario(salario)
        
        if total_salarios <= self.presupuesto:
            self.presupuesto -= total_salarios
            print("Se ha realizado el pago de la nómina.")
        else:
            print("No hay suficiente presupuesto para pagar la nómina.")
    
    def agregar_presupuesto(self, cantidad):
        self.presupuesto += cantidad

nomina = Nomina(10000)

while True:
    print("1. Agregar empleado")
    print("2. Mostrar empleados")
    print("3. Pagar nómina")
    print("4. Agregar presupuesto")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        rol = input("Ingrese el rol del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        cedula = input("Ingrese la cédula del empleado: ")
        balance = float(input("Ingrese el balance del empleado: "))
        
        empleado = Empleado(rol, nombre, cedula, balance)
        nomina.agregar_empleado(empleado)
    elif opcion == 2:
        nomina.mostrar_empleados()
    elif opcion == 3:
        nomina.pagar_nomina()
    elif opcion == 4:
        cantidad = float(input("Ingrese la cantidad a agregar al presupuesto: "))
        nomina.agregar_presupuesto(cantidad)
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

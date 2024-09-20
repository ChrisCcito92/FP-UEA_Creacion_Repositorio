# Función para calcular el valor con un descuento preestablecido del 10%
def calcular_descuento(val_compra):
    val_total = val_compra / 1.1  # Aplicar descuento del 10%
    print(f'El valor a pagar, incluido el descuento del {val_tota:.2f}%, es: {val_total:.2f}')


# Solicitar el monto de la compra
valor_final = calcular_descuento(float(input("Ingrese el monto de la compra: ")))


# Función para calcular el valor con un descuento ingresado por el usuario
def calcular_descuento1(val_compra1, porcentaje_desc):
    val_total1 = val_compra1 / (1 + (porcentaje_desc / 100))  # Aplicar descuento dinámico
    print(f'El valor a pagar, incluido el descuento del {porcentaje_desc}%, es: {val_total1:.2f}')

# Solicitar el monto de la compra y el porcentaje de descuento
mt = float(input("Ingrese el monto de la compra: "))
pd = float(input("Ingrese el porcentaje de descuento: "))
valor_final1 = calcular_descuento1(mt, pd)

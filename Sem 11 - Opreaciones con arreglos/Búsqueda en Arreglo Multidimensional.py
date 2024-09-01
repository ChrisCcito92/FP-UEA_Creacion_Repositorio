# Matriz ingresada 3*3
matriz = [
    [6,8,1],
    [3,7,2],
    [0,5,4]
]

# Definimos una función para buscar el valor
def buscar_valor(matriz, num_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num_buscado:
                return i, j
    return None  # Devuelve None si el valor no se encuentra

# Indicamos el número que queremos buscar en la matriz
num_buscado = int (input("Ingrese el número a buscar: "))

# Llamamos a la funcuón y desplegamos el resutaldo en caso de encontrarlo
posicion = buscar_valor(matriz, num_buscado)

if posicion:
    print("El valor buscado se encuentra en la poscición", posicion)
else:
    print ("Valor no enconrtado")
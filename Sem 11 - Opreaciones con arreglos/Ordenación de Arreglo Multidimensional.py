# Matriz ingresada 3*3
matriz = [
    [6,8,1],
    [3,7,2],
    [0,5,4]
]
# Usamos la función usando buble sort
def buble_sort(fila):
    num = len(fila)
    for i in range(num):
        for j in range(num-1, i, -1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)

# Imprimimos las matrices
print("Matriz original ", matriz)
buble_sort(matriz[1])
print("Matriz ordenada de mayor a menor ", matriz)
# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 19},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 14},
            {"dia": "Viernes", "temp": 11},
            {"dia": "Sábado", "temp": 8},
            {"dia": "Domingo", "temp": 9}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 11},
            {"dia": "Martes", "temp": 13},
            {"dia": "Miércoles", "temp": 10},
            {"dia": "Jueves", "temp": 15},
            {"dia": "Viernes", "temp": 18},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 19},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 14},
            {"dia": "Jueves", "temp": 16},
            {"dia": "Viernes", "temp": 19},
            {"dia": "Sábado", "temp": 17},
            {"dia": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 11},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 12},
            {"dia": "Jueves", "temp": 10},
            {"dia": "Viernes", "temp": 8},
            {"dia": "Sábado", "temp": 11},
            {"dia": "Domingo", "temp": 13}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 29},
            {"dia": "Jueves", "temp": 32},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 26}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 19},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 21},
            {"dia": "Jueves", "temp": 26},
            {"dia": "Viernes", "temp": 29},
            {"dia": "Sábado", "temp": 31},
            {"dia": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 26},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 28},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 23},
            {"dia": "Sábado", "temp": 29},
            {"dia": "Domingo", "temp": 31}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 29},
            {"dia": "Martes", "temp": 26},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 21},
            {"dia": "Viernes", "temp": 23},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 20}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 10},
            {"dia": "Jueves", "temp": 12},
            {"dia": "Viernes", "temp": 16},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 20}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 22},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 17},
            {"dia": "Domingo", "temp": 15}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 11},
            {"dia": "Miércoles", "temp": 14},
            {"dia": "Jueves", "temp": 12},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 16}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 19},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 21},
            {"dia": "Viernes", "temp": 16},
            {"dia": "Sábado", "temp": 17},
            {"dia": "Domingo", "temp": 14}
        ]
    ]
]

# Definimos la función que realiza el calculo de las tempreaturas y nos retorna el promedio por ciudad
def calcular_promedio (temperaturas,ciudad_idx):
    ciudad = temperaturas[ciudad_idx]
    suma_temperaturas = 0 # la variable para almacenar la suma de todas las temperaturas
    tot_dias = 0 # el contador que indicara cuantas temperatutras se ingresaron en la variable anterior
    for semana in ciudad:
        for dia in semana:
            suma_temperaturas += dia['temp'] # toma y suma la temperatura del diccionario en la variable
            tot_dias += 1 # cuenta los dias que va tomando
    promedio = suma_temperaturas / tot_dias
    return promedio

# generamos un menu interactivo que nos indica la ciudad que debemos tomar
while True:
    print("Seleccione una ciudad")
    print("1- Quito")
    print("2- Guayaquil")
    print("3- Cuenca")
    print("4- Salir")
    opcion = input("Ingrese la opción: ")
# nos despliega la información de la ciudad de Quito, así como el promedio de las temperaturas diarias de las 4 semanas
    if opcion == "1":
        promedio = calcular_promedio(temperaturas, ciudad_idx=0)
        print(f'El promedio de la temperatura en Quito es: {promedio:.2f}ªC')
# nos despliega la información de la ciudad de Guayaquil, así como el promedio de las temperaturas diarias de las 4 semanas
    elif opcion == "2":
        promedio = calcular_promedio(temperaturas, ciudad_idx=1)
        print(f'El promedio de la temperatura en Guayaquil es: {promedio:.2f}ªC')
# nos despliega la información de la ciudad de Cuenca, así como el promedio de las temperaturas diarias de las 4 semanas
    elif opcion == "3":
        promedio = calcular_promedio(temperaturas, ciudad_idx=2)
        print(f'El promedio de la temperatura en Cuenca es: {promedio:.2f}ªC')
# esta opción es para terminar el programa
    elif opcion == "4":
        print("Saliendo del programa...")
        break
# no despliega esta opción en caso de haber ingresado otro valor diferente al mostrado en el menú
    else:
        print("Opción no válida. Intente nuevamente.")
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

# Funciòn que calcula el promedio de temperaturas por cada semana
def calcular_prome(ciudad):
    for semana_index, semana in enumerate(ciudad, start=1):
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"Semana {semana_index}: Promedio de temperatura: {promedio: .2f}ªC")

# Menú y llamado a la función de cálculo
while True:
    print("Seleccione una ciudad")
    print("1- Quito")
    print("2- Guayaquil")
    print("3- Cuenca")
    print("4- Salir")
    opcion = input("Ingrese la opción: ")
    if opcion == "1":
        print("Ciudad elegida: Quito")
        calcular_prome(temperaturas[0])
    elif opcion == "2":
        print("Ciudad elegida: Guayaquil")
        calcular_prome(temperaturas[1])
    elif opcion == "3":
        print("Ciudad elegida: Cuenca")
        calcular_prome(temperaturas[2])
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")

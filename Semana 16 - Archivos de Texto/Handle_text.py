#creo el archivo denominado my_notes, se usa el método w para escribir, lo abro
archivo = open('my_notes', 'w')
#ingreso información en el archivo con eso uso de write y "\n" que da un salto de linea
archivo.write("Dato curisoso: Una nube pesa alrededor de un millón de toneladas.\n")
archivo.write("Refrán: Cuando una puerta se cierra, cientos se abren.\n")
archivo.write("Chiste: ¿Qué hace un mudo bailando? Una mudanza.\n")
#cierro el archivo
archivo.close()

#abro el archivo denominado my_notes, se usa el método r para leer
archivo = open('my_notes', 'r')
#con eso uso de seek, ubico el curso al inicio de la primera linea en la posición 0 y voy leyendo de linea en linea, las mismas que asigno a una variable distinta
archivo.seek(0)
texto1 = archivo.readline()
texto2 = archivo.readline()
texto3 = archivo.readline()
#imprimo en pantalla las tres variables con los textos que cada una posee
print(texto1)
print(texto2)
print(texto3)
#cierro el archivo
archivo.close()
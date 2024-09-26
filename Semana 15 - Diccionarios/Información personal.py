#Creación de un diccionario con: nombre, edad, ciudad y profesión
informacion_personal ={"Nombre": "Juan Romero", "Edad": 28, "Ciudad": "Ambato", "Profesión": "Ingeniero Industrial"}
print(informacion_personal)

# Reemplazamos el valor de la clave: Ciudad de "Ambato" por "Puyo"
print("Cambio de ciudad")
informacion_personal["Ciudad"] = "Puyo"
print(informacion_personal)

#Cambiamos la clave de "profesión" por "ocupación"
print("Cambio de profesión por ocupación")
informacion_personal['Ocupación'] = informacion_personal.pop('Profesión')
print(informacion_personal)

# Consultamos si la clave "Telefono" esta crada, solo enviamos un mensaje que ya existe caso contrario la creamos
print("Creación de nueva clave Telefono")
if "Teléfono" in informacion_personal:
    print("La clave ya está creada")
else:
    informacion_personal['Teléfono'] = '098 765 4321'
    print(informacion_personal)

# Eliminamos la clave y valor correspondientes a edad
print("Eliminación de edad")
del informacion_personal['Edad']
print(informacion_personal)
def saludar(nombre):
    return "Hola {} perdon por la tardanza, me perdi en el sendero de la vida".format(nombre)

print("Ingresa tu nombre")
nombre = input()
print(saludar(nombre))
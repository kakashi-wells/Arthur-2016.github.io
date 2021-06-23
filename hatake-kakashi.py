def saludar(nombre):
    return "Hola {} Aquellos que rompen las reglas son escoria, pero los que abandonan a un amigo son peor que escoria.".format(nombre)

print("Ingresa tu nombre")
nombre = input()
print(saludar(nombre))
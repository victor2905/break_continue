#Ejemplo para break
print("While con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        break

    print("Valor de la variable: ",contador)

print("Fin del programa, la sentencia break se ha ejecutado")

#Ejemplo para continue

print("While con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue

    print("Valor de la variable: ",contador)

print("Fin del programa, la sentencia continue se ha ejecutado")

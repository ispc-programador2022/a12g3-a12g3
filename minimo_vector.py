def minimo_vector(lista):
    # Asigno el 1er elemento de la lista como valor minimo
    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo
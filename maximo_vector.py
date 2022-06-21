def maximo_vector(lista):
    # Asigno el 1er elemento de la lista como valor minimo
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo
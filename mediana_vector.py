def mediana_vector(lista):
    lista.sort()
    # Obtener longitud de la lista
    longitud = len(lista)
    mitad = int(longitud / 2)
    # Si la longitud es par, promediar elementos centrales
    if longitud % 2 == 0:
        mediana = (lista[mitad - 1]+lista[mitad]) / 2
    else:
        mediana = lista[mitad]
    return mediana  
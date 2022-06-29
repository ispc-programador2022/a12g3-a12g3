

def suma_combinaciones(lista_aleatorios: list[int]) -> list:
    '''
    Toma una lista de 50 números aleatorios y devuelve una lista
    con las sumas de las combinaciones de a dos de los elementos
    de la lista. Los elementos no se repiten.
    '''

    # busco los elementos que no se repiten en la lista
    el_unicos = set(lista_aleatorios)
    el_unicos = list(el_unicos)
    sumas = []
    i = 0
    while (i < len(el_unicos)-1):
        for e in el_unicos[i+1:]:
            suma = el_unicos[i] + el_unicos[i+1]
            sumas.append(suma)
        i += 1
    sumas = list(set(sumas))
    return sumas

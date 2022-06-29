

def suma_combinaciones(lista_aleatorios: list[int]) -> list:
    '''
    Toma una lista y devuelve una lista
    con los productos de las combinaciones de a dos de los elementos
    de la lista. Los elementos no se repiten.
    '''

    # busco los elementos que no se repiten en la lista
    el_unicos = set(lista_aleatorios)
    el_unicos = list(el_unicos)
    productos = []
    i = 0
    while (i < len(el_unicos)-1):
        for e in el_unicos[i+1:]:
            producto = el_unicos[i] * el_unicos[i+1]
            productos.append(producto)
        i += 1
    productos = list(set(productos))
    return productos

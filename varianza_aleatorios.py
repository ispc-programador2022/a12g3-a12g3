from media import media


def varianza(lista: list[int]) -> int:
    '''
    Toma una lista de números enteros.
    Devuelve la varianza de la lista
    '''
    med = media(lista)
    var = 0
    for e in lista:
        var += (e - med)**2
    var = var / len(lista)
    return var

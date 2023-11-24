def busca(lista, elemento):
    for r in range(len(lista)):
        if lista[r] == elemento:
            return r
    return False
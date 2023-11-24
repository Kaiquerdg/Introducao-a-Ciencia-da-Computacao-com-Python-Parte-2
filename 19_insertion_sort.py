def insertion_sort(lista):

    for r in range(len(lista)):
        for x in range(r, 0, -1):
            if lista[x] < lista[x-1]:
                lista[x], lista[x-1] = lista[x-1], lista[x]

    return lista
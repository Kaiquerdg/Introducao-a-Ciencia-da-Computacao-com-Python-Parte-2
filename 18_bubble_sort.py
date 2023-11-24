def bubble_sort(lista):
    for r in range(len(lista)-1, 0, -1):
        for x in range(r):
            if lista[x] > lista[x+1]:
                lista[x], lista[x+1] = lista[x+1], lista[x]
                print(lista)
    return lista
def ordena(lista):
    tamanho = len(lista)

    for r in range(tamanho - 1):
        menor = r
    
        for n in range(r + 1, tamanho):
            if lista[n] < lista[menor]:
                menor = n

        lista[r], lista[menor] = lista[menor], lista[r]
    return lista
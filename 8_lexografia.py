def primeiro_lex(lista):
    menor = lista[0]
    for l in lista:
        if menor > l:
            menor = l
    return menor
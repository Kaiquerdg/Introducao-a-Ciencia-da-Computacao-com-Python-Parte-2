import random # módulo para deixar a sequencia aleatoria

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 1000))
    return lista
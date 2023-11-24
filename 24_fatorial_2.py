def fatorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("Não existe fatorial de números negativos.")
    else:
        return n * fatorial(n-1)
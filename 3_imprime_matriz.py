def imprime_matriz(m):
    
    lin = len(m)
    col = len(m[0])

    for i in range(lin):
        for j in range(col):
            if j == col - 1:
                print(m[i][j], end = "")
            else:
                print(m[i][j], end = " ")
        print()
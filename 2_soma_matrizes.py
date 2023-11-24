def dimensoes(matriz):
    i = len(matriz)
    j = len(matriz[0])
    return "{}X{}".format(i, j)

def soma_matrizes(m1, m2):
    dimensaom1 = dimensoes(m1)
    dimensaom2 = dimensoes(m2)
    
    if dimensaom1 == dimensaom2:
        soma = []
        
        for i in range(len(m1)):
            lin = []
            
            for j in range(len(m1[0])):
                m3 = m1[i][j] + m2[i][j]
                lin.append(m3)
                
            soma.append(lin)
        
        return soma
    else:
        return False
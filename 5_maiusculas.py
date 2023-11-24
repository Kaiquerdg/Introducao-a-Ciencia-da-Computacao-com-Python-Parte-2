def maiusculas(frase):
    upper = []
    
    for f in range(len(frase)):
        letras = frase[f]
        ordem = ord(letras)

        if ordem >= 65 and ordem <= 90:
            upper.append(letras)
            
    upper = "".join(upper) # Une como uma string vazia
            
    return upper
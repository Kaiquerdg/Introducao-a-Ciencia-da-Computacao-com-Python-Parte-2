def conta_letras(frase, contar="vogais"):
    lista_vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vogais = 0
    consoantes = 0
    
    frase = frase.replace(" ", "") # Se não tirar os espaços, o resultado não bate
    
    for f in range(len(frase)):
        caracteres = frase[f]
        if caracteres in lista_vogais:
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1
    
    if contar == "vogais":
        return vogais
    elif contar == "consoantes":
        return consoantes
    
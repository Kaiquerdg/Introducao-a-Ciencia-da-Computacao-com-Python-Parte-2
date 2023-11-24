def menor_nome(nomes):
    menor = nomes[0]
    comprimento_menor = len(nomes[0])
    
    for n in nomes:
        n = n.strip()
        
        if len(n) < comprimento_menor:
            comprimento_menor = len(n)
            menor = n
        
    menor = menor.capitalize()
    
    return menor
        
    


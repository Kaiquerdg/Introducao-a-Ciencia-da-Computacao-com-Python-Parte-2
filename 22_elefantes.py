def incomodam(n):
    if n <= 0:
        return ""
    elif n > 0:
        return "incomodam " + incomodam(n - 1)

def elefantes(n):
    x = 1
    muito_mais = ""
    muita_gente = ""
    if n == 1:
        return "Um elefante incomoda muita gente\n"
    elif n <= 0:
        return ""
    elif n > 1:
        while x < n:
            x = x + 1
            if x < n:
                muito_mais = str(x) + " elefantes " + incomodam(n) + "muito mais\n"
                muita_gente = str(x) + " elefantes incomodam muita gente\n"
            else:
                muito_mais = str(x) + " elefantes " + incomodam(n) + "muito mais\n"
        return elefantes(n-1) + muita_gente + muito_mais
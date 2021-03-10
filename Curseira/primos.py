

""" Essa função é para ver se o numero é primo ou não ! True ou False."""

def primo(numero): #Essa função é para ver se o numero é primo ou não ! True ou False.
    inicio = 1
    contador_divisor = 0
    while inicio <= numero:
        if numero % inicio == 0:
            contador_divisor = contador_divisor + 1
        inicio = inicio + 1
    
    if contador_divisor <= 2:
        return True
    else:
        return False

numero = int(input("digite "))

primo(numero)
print(primo(numero))

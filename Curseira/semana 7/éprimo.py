
n = int(input("digite um numero para ver se é primo "))
inicio = 1
contador_divisor = 0
while inicio <= n:
    if n % inicio ==0:
        contador_divisor = contador_divisor + 1
    inicio = inicio + 1

if contador_divisor <= 2:
    print(n,"é primo!")
else:
    print(n,"não é primo")

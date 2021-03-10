"""Eu quero que você faça programa que vá receber do usuário, que vai digitar uma sequência de números
e para cada número que ele digite eu quero que você imprima o fatorial desse número"""

n = 1
while n >= 0:
    n = int(input("Digite um numero!"))
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n 
        n = n - 1
    print(fatorial)


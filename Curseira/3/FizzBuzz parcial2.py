'''Exercícios 2 - FizzBuzz parcial, parte 1
Receba um número inteiro na entrada e imprima

Fizz

se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.'''

n = int(input(""))

if n % 3 == 0:
    print("Fizz")
else:
    print(n)
'''Exercício 2 - Invertendo sequência
Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa.
A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

Exemplo:

Digite um número: 1
Digite um número: 7
Digite um número: 4
Digite um número: 0

4
7
1

'''
n = None
lista = []
while n != 0:
    n = int(input("Digite um número: "))
    lista.append(n)
del(lista[-1])
lista.reverse()

for x in lista:
    print(x)






'''Exercício 1 - Máximo
Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Exemplos de execução no shell do Python:'''

'''
>>> maximo(3, 4)
4
>>> maximo(0, -1)
0
'''

def maximo(a,b):
    if a > b:
        return a
    else:
        a < b
        return b

a = int(input())
b = int(input())

print(maximo(a,b))


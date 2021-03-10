"""Exercício 2 - Primos
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e 
devolve o maior número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:
>>> maior_primo(100)
97
>>> maior_primo(7)
7

Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando 
se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável 
é o maior primo encontrado.
"""

def maior_primo(n):
    ax1 = n
    while ax1 >= 2:
        if éPrimo(ax1):
            return ax1
        ax1 = ax1 - 1
    return 2

    



def éPrimo(x): # para saber se o numero é primo.
    inicio = 1
    conta_primos = 0
    while inicio <= x:
        if x % inicio == 0:
            conta_primos = conta_primos + 1 
        inicio = inicio + 1 
    

    if conta_primos <= 2 :
        return True
    

    



numero = int(input("Digite ")) 
    


print(maior_primo(numero))
'''Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente'''

lista = []
cont = 0

while cont < 3:
    n = int(input("digite: "))
    lista.append(n)
    cont = cont + 1

if lista[0] < lista[1] and lista[1] <  lista[2] :
    print("crescente")
else:
    print("não está em ordem crescente")



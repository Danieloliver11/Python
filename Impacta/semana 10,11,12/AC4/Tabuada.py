#Faça um programa que leia um número inteiro e imprima a tabuada de multiplicação
# deste número. Suponha que o número lido da entrada é maior que zero.
def tabu():
    n = int(input("Digite"))
    for x in range(1, 10):
        resu = n * x
        print("{}X{}={}".format(n, x, resu))


tabu()

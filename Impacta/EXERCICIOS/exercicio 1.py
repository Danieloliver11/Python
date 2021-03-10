#Faça um programa que leia três números inteiros e encontra o menor deles.
#Sugestão: Sejam 3 números A, B e C. A ideia principal é: verificar se A é menor que B e C e se não for,
#verificar entre B e C

a = int(input("digite o primeiro numero "))
b = int(input("digite o segundo numero "))
c = int(input("digite o terceiro numero "))

if a < b or c:
    print("{} é o menor numero entre {} e {}".format(a,b,c))
else:
    print("{}  é maior que {} e {}".format(a,b,c))
    if b > c:
        print("{} é maior que {}".format(b,c))
    else:
        print("{} é maior que {}".format(c,b))

#cria um programa onde o usuario possa digitar varios valores numericos e cadastra-os
# em uma lista. caso o numero já exista la dentro, ele não será adicionado.
#no final,serão exibidos em ordem crecente.


lista = []

while True:
    n = int(input("digite o numero"))
    if n not in lista:
        lista.append(n)
        lista.sort()
    else:
        print("Esse numero ja contem: ")
        p = input("Deseja continuar? [S/N]")
        if p in "Nn" :
            break



print(lista)











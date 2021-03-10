lista =  ["rpg","é","muito","legal",]
print("primeira", lista)
lista[1] ="foda" #substitui  o que tem na lista n aposição desejada
print("segundo",lista)
lista.insert(1,"RPG") # troca o que esta na posição por algo que voce quer colocar, mas não apaga e retira nada da lista.
print("terceiro",lista)
lista.append("gosto muito") #aqui acrecenta coisas QUE SEMPRE VAI PARA O FINAL DA LISTA.
print("quarto",lista)
del(lista[0]) #aqui é diferente ja que Del pode usar para outras tarefas. (ele deleta o que esta na posição.
print("quinto",lista) # Inverte toda alista
lista.reverse()
print("sexto", lista)
lista.sort() # Esse comando coloca em ordem crescente as informações na lista.
print("setimo",lista)


valor= []

valor.append(int(input("digite um valor ")))
valor.append(int(input("digite um valor ")))
valor.append(int(input("digite um valor ")))
valor.append(int(input("digite um valor ")))

n = len(lista) # o comando Len é para saber quantos objetos tem na lista. e tem que ser jogado em uma variavel para amarcenar
# o resultado (n)
print("numero de intens na lista", n)
print(valor)
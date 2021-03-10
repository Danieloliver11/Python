#AC 4 Lógica de programação

n = int(input('Digite a quantidade de nomes que irá digitar:'))
list = []

#Digitar números entre 3 e 10.
while n <3 or n>10:
  n = int(input('Digite um número entre 3 e 10:'))

#lista de n elemento.
for x in range(1,n):
   valor = input('Digite um nome:')
   list.append(valor)
print('Nomes digitados pelo usuario:',list)

#Inserir "teste" no indice 3.
list.insert(3,'Teste')
print('lista depois de inserir teste:',list)

#excluir elemento no indice 2.
del list[2]
print('Lista depois de excluir indice 2:',list)

#Verifique quantas vezes você digitou o nome 'Ana'. Se for maior que 0, mostre o índice da primeira ocorrência,
#Se for 0, mostre uma frase informando que o nome Ana não existe na lista.
r = list.count('Ana')
if r >0:
  print('O indice da primeira ocorrência do nome Ana:',list.index('Ana'))
else:
 print('O nome Ana não exite na lista.')

#No final, mostre a lista ordenada.
list.sort()
print(list)
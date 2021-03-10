#(Escreva um programa que irá receber duas entradas: uma sequencia de caracteres e um único caractere e irá
# contar quantas vezes o caractere aparece na sequencia. Você deve escrever uma função que irá receber como parâmetros
# a sequencia e o caractere, e retornar o número de ocorrências pedido. No código principal do programa, faça a leitura
# dos dados de entrada (input's), chame a sua função para contar o número de ocorrências, e em seguida imprima o resultado pedido.
#OBS: Não é permitido o uso do .count() para realizar a contagem.
#DICA: A ideia é criar uma função que faça a mesma coisa que o .count(), portanto você pode usar o .count() para comparar
# os seus resultados e validar a sua função. Para fazer a contagem, faça um laço (for ou while) iterando sobre a sequência
# e criei um contador para guardar quantas vezes o caractere foi encontrado.)

#minha terra tem palmeiras
# q

nome = input("Digite um nome")
letra = input("digite uma letra que verei se tem e quantas vezes tem essa letra")
cont = 0
for x in nome:
    if x == letra:
        cont = cont + 1

if cont > 0:
    print(cont)
else:
    print("Não tem nenhuma letra")
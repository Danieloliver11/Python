'''Exercício 3
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

Digite um número inteiro: 123
6

Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, 
aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, 
ou seja, tudo que é maior ou igual ao divisor.'''

n = int(input())

soma = 0

while n > 0: # é preciso um laço para ir tirando o ultimo numero 
    sobra = n % 10 # aqui é retirado no laço o ultimo numero 
    n = n // 10 # aqui ele não ira pegar o ultimo numeor 
    soma = soma + sobra # aqui ele ira adicionar sempre o ultimo numero retirado no laço da variavel (sobra)
print(soma)



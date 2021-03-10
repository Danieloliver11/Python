'''(Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:

Exemplo 1:

Entrada de Dados:
Digite um número inteiro: 78615

Saída de Dados:
O dígito das dezenas é 1

Exemplo 2:

Entrada de Dados:
Digite um número inteiro: 2

Saída de Dados:
O dígito das dezenas é 0

Dica: O operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor. 
O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.)'''

n = int(input("Digite um número inteiro: ")) 
d = (n // 10) % 10 
print("O dígito das dezenas é:",d) 


"""(O que você faz quando quer mover para a esquerda o ponto/vírgula em um número? Divide por 10...
1234 / 10 = 123.4

Mas essa é uma divisão racional, e resulta em um número racional.

Entretanto se fizermos a divisão inteira por 10 o que acontece é que eliminamos o último dígito, pois não consideramos parte fracionária em números
inteiros.

1234 // 10 = 123

Em divisão inteira obtém-se o resultado (ou quociente) e sobra um resto 
(e usamos o resto da divisão inteira por 10 para obter o último digito do número dividendo).)"""
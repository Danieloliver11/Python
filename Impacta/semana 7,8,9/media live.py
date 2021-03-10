# Função para somar os n números que serão digitados pelo usuário
# Obs: range vai até n+1, para considerar o valor de n

def soma(n):
    soma_total = 0

    for c in range(1, n + 1):
        n1 = int(input('Digite um número: '))
        soma_total = soma_total + n1

    return soma_total


# A média é a soma de todos os valores dividido pela quantidade de valores somado
def media(soma_total, n):
    result = soma_total / n

    return result


# algoritmo principal
n = int(input('Digite quantos valores você quer digitar para calcular a média: '))

soma_total = soma(n)
media_total = media(soma_total, n)

print('A média é: ', media_total)


# Função para somar os números que serão digitados pelo usuário. Não sabe quantos números serão,
# mas cada vez que digitar um número, deve incrementar o valor de n, que é a qtde de números
# No final, retornar a soma de todos os números digitados, e q qtde de números digitados
# Em Python, para retornar mais de um valor, é só colocar vírgula entre os valores. Veja no return

def soma():
    soma_total = 0
    continuar = True
    n = 0

    while continuar == True:
        n1 = int(input('Digite um número: '))
        soma_total = soma_total + n1
        n = n + 1  # quantidade de números que sendo digitado

        res = input('Continuar digitando número? N ou n encerra, outra valor, continua.')
        if res == 'n' or res == 'N':
            continuar = False

    return soma_total, n


# A média é a soma de todos os valores dividido pela quantidade de valores somado
def media(soma_total, n):
    result = soma_total / n

    return result


# algoritmo principal

# funçao soma vai retornar dois valores, o primeiro é a soma total e o segundo, é a qtde de números digitados
soma_total, n = soma()
media_total = media(soma_total, n)

print('A média é: ', media_total)
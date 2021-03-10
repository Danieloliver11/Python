#Crie um programa que tenha uma única função, além da principal, que receberá como parâmetro um natural n (0<=n<=2^30)
# e devolverá a quantidade de dígitos de n. O programa exibirá o retorno da função. Observações: (a) apenas um laço de repetição; (b) sem matrizes; (c) função iterativa.
#Formato de entrada : 12345678
#Formato de saída: 8

numero = (input("digite "))

for x in numero:
    n = len(numero)
print("o que voce digitou tem ",n,"digitos")
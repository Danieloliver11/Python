#Faça um programa de resolução de tabuada. O programa deve inicialmente receber 2 números que indicam de quais números
# devem ser impressas a tabuada. Por exemplo, se forem recebidos os valores 2 e 5, seu programa deve imprimir a tabuada
# de 2, 3, 4 e 5. O programa só deve aceitar valores entre 1 e 9. Enquanto o usuário digitar valores que não sejam
# esses, emita uma mensagem de erro

a1 = 0
a2 = 0
while a1 < 1 or a1 > 9:
    a1 = int(input())
    if a1 < 1 or a1 > 9:
        print("Insira um número inicial entre 1 e 9") #nao deixa passar se for menor que n1 e maior que na1

while a2 < 1 or a2 > 9:
    a2 = int(input())
    if a2 < 1 or a2 > 9:
        print("Insira um número final entre 1 e 9") # aqui faz a mesma coisa so que agora com a2

if a1 > a2:
    print("Nenhuma tabuada nesse intervalo")
#aqui faz as tabuadas
for t in range(a1, a2 + 1):
    for c in range(1, 10):
        print(t, "x", c, "=", t * c)
    print("")



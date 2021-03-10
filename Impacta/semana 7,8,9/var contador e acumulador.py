def contador():
    print("*************************************** \n Pirmeiro executamos a FUNÇÃO Contador  \n **************************************")
    num = int(input("Digite um numero : "))
    n = int(input("Digite um numero maior que você digitou pela primeira vez: "))
    for nume in range(num,n):
        print(num)
        num = num + 1


def acumulador():
    print("*************************************** \n Segundo executamos a FUNÇÃO Acumulador  \n **************************************")

    num = int(input("Digite um numero : "))
    n = int(input("Digite um numero maior que você digitou pela primeira vez: "))
    acumu = 1
    for nume in range(num, n):
        print(num, acumu)
        acumu = acumu + num
        num = num + 1


contador()
acumulador()

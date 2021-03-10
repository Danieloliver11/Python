'''
Faça um algoritmo para ler um número que é um código de usuário.

Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada 
a mensagem "Usuário inválido!" e o sistema será encerrado.

Caso o código seja correto, deve ser lido outro valor que é a senha.

Se a senha estiver correta (a certa é 9999), deve ser exibida a mensagem "Acesso permitido".

Se a senha estiver incorreta deve ser exibida a mensagem "Senha incorreta", e também uma mensagem com as seguintes 
opções:

1 - tentar novamente
0 - encerrar sistema

https://www.youtube.com/watch?v=IlL7eja1UJA&ab_channel=DevMedia


'''


def codigo(coo):
    if coo != 1234:
        print("Usuário inválido!")
    else:
        input(senha(coo))
        


def senha(sem):
    if sem != 9999:
        pirnt("Senha incorreta")
        deci = int(input(("1 - tentar novamente \n 0 - encerrar sistema"))



co = int(input("Digite o codigo: "))
codigo(co)




"""senha = 0

cod = int(input("Digite o codigo: "))

if cod == 1234:
    senha = int(input("Digite A senha "))
    while senha != 9999:
        print("Senha incorreta")
        print("1 - tentar novamente\n0 - encerrar sistema")
        res = int(input())
        if res == 1:
            senha = int(input("Digite A senha "))
        else:
            print("Sistema encerrado")
        
    

    print("Acesso permitido")
else:
    print("Usuário inválido!")'''
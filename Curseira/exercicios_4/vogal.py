'''Exercício 3 - Vogais
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False 
se for uma consoante.

Exemplos de execução no shell de Python

>>> vogal("a")
True
>>> vogal("b")
False
>>> vogal("E")
True

Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.'''

def vogal(aa):
    if aa == 'a' or aa == 'e' or aa =='i' or aa =='o' or aa =='u' or aa == 'A' or aa == 'E' or aa =='I' or aa =='O' or aa =='U' :
        aa = True
        return aa
    else:
        aa = False
        return False

aa = input()

print(vogal(aa))


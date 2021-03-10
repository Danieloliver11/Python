#exercicios python 04, Dissecando uma variável.

print('Escreve segundo o pedido do texto. ele dara False ou True se o que ele esta pedindo esta ou não esta correto.')
a = input('escreva um numero decimal:')
print(a.isdecimal())
aa = input('escrwva algo que não seja numero descimal:')
print(aa.isdecimal())

b = input('esceva algo com letra maiuscula:')
print(b.isupper())
bb = input ('escreva algo que nao esteja em letras maiusculas:')
print(bb.isupper())

c = input('escreva algo com letras pequenas:')
print(c.islower())
cc = input('escreva alguma letra minuscula:')
print(cc.islower())
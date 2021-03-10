
num = int(input("escreva um numeor que possa ser dividido por 3 e 5:  "))

if num%3==0:
    print(" o numero 3 é   divisiveis por {}".format(num))

elif num%5==0:
    print( "o nuemro 5 é  divisiveis por {}".format(num))
else:
    print(" o numero {} não é divisivel por 3 e 5".format(num))

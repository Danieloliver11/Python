
salar = float(input())

if (salar <= 1751.81):
    desconto = (8*salar/100)
    print("Desconto do INSS: R$ {:.2F}".format(desconto))
elif (salar >= float(1751.82) and salar <= float(2919.72)):
    desconto = (9*salar/100)
    print("Desconto do INSS: R$ {:.2F}".format(desconto))
elif ( salar >= float(2919.73) and salar <= float(5839.45)):
    desconto = (11*salar/100)
    print("Desconto do INSS: R$ {:.2F}".format(desconto))
elif (salar > float(5839.45)):
    desconto = (11*5839.45/100)
    print("Desconto do INSS: R$ {:.2F}".format(desconto))
#7567.30


#Desconto do INSS: R$ 120.00

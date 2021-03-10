ano = int(input("Qual o ano do seu carro?  "))
valor = float(input("Qual o valor do seu carro? "))

if (ano >= int(2010)):
    novova =  (valor*3.5/100)
    print("O carro de {}, do valor R$ {:.2f}, deve pagar uma taxa de R$ {:.2f}".format(ano,valor,novova))
else:
    novova =  (valor*2.5/100)
    print("O carro de {}, do valor de R$ {:.2f}, deve pagar uma taxa de R$ {:.2f}".format(ano,valor,novova))

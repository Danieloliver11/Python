'''Para fazer esse cálculo, divida o valor do salário por 12 
e multiplique o resultado pelo número de meses trabalhados no ano.
Do 13º salário proporcional, será descontado INSS e IR, conforme o valor.'''


def cal_resci (a,b,fgts):
    resul = (a / 12)
    resu = (resul * b)
    poor =  fgts + (40 * 100) 
    total = resu + poor
    print(" o total que você tem direito é de" ,int(resu), "mais",poor,"de FGTS que no tatal você tera de recisão ",int(total))

sal = int(input("Qual o seu salario ? "))
anos_trab = int(input("Quntos anos completos você trabalhou nessa empresa (não contar com esse ano) ? "))

mese_tem = int(input("Meses trabalhados nesse ano " ))
fg = int(input("Qual é o sado do seu FGTS ? "))

meses = anos_trab * 12
quantidemeses = meses + mese_tem
    


cal_resci(sal,quantidemeses,fg)

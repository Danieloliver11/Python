'''(Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, 
dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato:
a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais,
vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.)'''
""" uma hora = um minuto 3.481 = segundo 59   <<<<<"""
""" 86400 é um dia """

segun = int(input()) 

dia = segun // 86400
res_segundo = segun % 86400
horas = res_segundo // 3600
rest_segundo = res_segundo % 3600
minutos = rest_segundo // 60
segundos = rest_segundo % 60


print("{} dias, {} horas, {} minutos e {} segundos.".format(dia,horas,minutos,segundos))


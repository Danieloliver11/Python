'''Exercício 1
Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado
 calcule e imprima (saída de dados) seu perímetro e sua área.
Observação: a saída deve estar no formato: "perímetro: x - área: y"'''

peri = int(input())

p = peri * 4
a = peri * peri 

print('perímetro: {} - área: {}'.format(p,a)) 

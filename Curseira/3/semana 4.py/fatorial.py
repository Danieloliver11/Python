'''
Exercício 1
Escreva um programa que receba um número natural nn na entrada e imprima n!n! () na saída.

Exemplo:


Dica: lembre-se que o  de 0 vale 1!'''

'''n = int(input("Digite o valor de n: "))
5
resul 1
resul 2
resul 6
resul 24
resul 120
''' 



""" outro jeito de fazer"""
n = int(input())

i = fat = 1 

while i <= n :
  fat = fat * i
  i = i + 1 
  print("resul",fat)
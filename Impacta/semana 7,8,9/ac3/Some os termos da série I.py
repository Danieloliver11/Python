n = int(input()) #5
soma = 1
x = 4
y = 5

for i in range(n - 1):
    soma = soma + 1 / x
    x = x + y
    y = y + 2
print("{:.6f}".format(soma)) #1.463611
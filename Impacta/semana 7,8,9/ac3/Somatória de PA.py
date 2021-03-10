r = int(input())
n= int(input())
list = []

for x in range(1,n+r,r):
    list.append(x)
soma = sum(list)
print("A somatoria da PA eh:",soma)
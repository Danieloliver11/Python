
n = int(input("digite :"))
cont = 0
auxi = 0

while auxi <= 9:
    while cont <= 9:
        resul = (n * cont)
        cont = cont + 1
        print(n,"X",cont,"=",resul)
        auxi = auxi + 1
    
    
    

""" 
n = int(input("digite :"))
m = int(input("digite :"))

for x in range(n, m + 1):
    for y in range(1,10):
        print(x,"X",y,"=",x*y)
        """
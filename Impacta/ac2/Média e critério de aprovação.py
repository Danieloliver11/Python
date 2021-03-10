p1 = float(input())
p2 = float(input())
p3 = float(input())
fre = float(input())  #peso 2 , 2 e 3 / 27.9
#frequencia minima 75%
#media minima 6.0
media = round((p1*2+p2*2+p3*3) / (2+2+3),1) #media ponderada round é para aredondar em 1 casa, o 1 esta por ultipo depois da virgula
frequencia = (fre*100)
print("Frequencia: {:.0f}%".format(frequencia))
print("Media: {:.1f}".format(media))

if (frequencia < float(75)):
    print("Aluno reprovado por falta!")
elif ((media > float(9))):
    print("Aluno aprovado com louvor!")
elif ((media >= float(6)) and (media <= float(9))):
    print("Aluno aprovado")
elif ((media >= 4) and (media < float(6))):
    print("Aluno de recuperação!")
elif ((media < float(4))):
    print("Aluno reprovado!")

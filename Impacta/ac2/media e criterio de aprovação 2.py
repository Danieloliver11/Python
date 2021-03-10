p1 = float(input())
p2 = float(input())
p3 = float(input())
fre = float(input())  #peso 2 , 2 e 3 / 27.9
#frequencia minima 75%
#media minima 6.0
media = round(((p1*2+p2*2+p3*3) / (2+2+3)),1
frequencia = (fre*100)

if (frequencia < float(75)):
    print("Aluno reprovado por falta!")
elif ((media > float(9))):
    print("Aluno aprovado com louvor!")
elif ((media >= float(6)) and (media <= float(9))):
    print("Aluno aprovado")
elif ((media >= float(4)) and (media < float(6))):
    print("Aluno de recuperação!")
elif ((media < float(4))):
    print("Aluno reprovado!")

print("media: {:.1f} frequencia: {:.0f}".format(media,frequencia))

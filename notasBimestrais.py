#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1= float(input("Qual foi sua nota no primeiro bimestre?"))
n2= float(input("Qual foi sua nota no segundo bimestre?"))
n3= float(input("Qual foi sua nota no terceiro bimestre?"))
n4= float(input("Qual foi sua nota no quarto bimestre?"))

media = (n1 + n2 + n3 + n4) / 4
print("Sua média foi {:.1f}" .format(media))

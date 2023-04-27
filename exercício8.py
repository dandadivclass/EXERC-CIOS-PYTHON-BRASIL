#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.

ganhoH = float(input("Quanto você ganha por hora?"))
horasM = float(input("Quantas horas você trabalhou nesse mês?"))

totalS = ganhoH * horasM
print("Você ganha, no total, o valor de R${} mensalmente!" .format(totalS))

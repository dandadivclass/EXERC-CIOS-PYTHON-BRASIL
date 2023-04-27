#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês...

gHora = float(input("Informe aqui quanto você ganha por hora:"))
nHoras = float(input("Informe também o total de horas trabalhadas por hora no mês:"))
totalSalario = gHora * nHoras

print("O SEU SALÁRIO BRUTO SE CONFIGURA COMO R${}" .format(totalSalario))

  #descontos a serem pagos
IR = totalSalario * 11/100          #ou 0.11. sempre multiplicar em cima do valor!
INSS = totalSalario * 8/100         #ou 0.08
Sindicato = totalSalario * 5/100    #ou 0.05

print("Você paga R${} de imposto de renda!" .format(IR))
print("Você paga R${} ao INSS" .format(INSS))
print("E ao sindicato você paga R${}" .format(Sindicato))

salarioLiquido = (totalSalario - IR) - (INSS) - (Sindicato)
print("Assim, ficamos com o total de R${} configurado como seu Salário Líquido!" .format(salarioLiquido))

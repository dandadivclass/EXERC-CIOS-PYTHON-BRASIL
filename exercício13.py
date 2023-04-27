#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
  Para homens: (72.7*h) - 58
  Para mulheres: (62.1*h) - 44.7
  
print("QUER SABER SEU PESO IDEAL? VENHA COM A GENTE pt2")
altura = float(input("Informe a sua altura"))
peso = (72.7 * altura) - 58
peso2 = (62.1*altura) - 44.7
print("Se você for um Homem, seu peso ideal de acordo com sua altura é {:.2f}kg!" .format(peso))
print("Se você for uma Mulher, seu peso ideal de acordo com sua altura é {:.2f}kg!" .format(peso2))
 

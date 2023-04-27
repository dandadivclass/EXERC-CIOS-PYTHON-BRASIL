nome = input("Olá! Informe o seu nome por favor:")
salario_fixo = float(input("{}, qual a sua renda fixa?" .format(nome)))
vendas = float(input("Agora, coloque aqui em dinheiro as vendas efetuadas pela sua loja esse mês:"))

total_receber = vendas * 0.15
salario_vendas = salario_fixo + total_receber

print("{}, o seu total a receber junto a 15% de comissão das suas vendas é de R${:.2f}" .format(nome, salario_vendas))

area_metro2 = float(input("Qual a área que você quer pintar em metros quadrados?"))
tinta2 = (1/6 * area_metro2) * 80
galoes = (3/6 * area_metro2) * 25
tin_gal = (1/6 * area_metro2) + (3.6 * area_metro2) * (105 * 0.1)
print("SE VOCÊ DESEJA COMPRAR LATAS DE TINTAS O VALOR FICARÁ R${:.2f} PARA A ÁREA DESEJADA!" .format(tinta2))
print("SE VOCÊ DESEJA COMPRAR GALÕES DE TINTA O VALOR FICARÁ R${:.2f} PARA A ÁREA DESEJADA" .format(galoes))
print("SE VOCÊ DESEJA COMPRAR GALÕES E LATAS DE TINTA O VALOR FICARÁ R${:.0f} PARA A ÁREA DESEJADA" .format(tin_gal))

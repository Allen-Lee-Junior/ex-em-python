preço = float(input('Qual é o preço do produto RS'))
desconto = preço - (preço * 5 / 100)
print('O produto que custava {:.2f} na promoção com  desconto de 5% vai custar {:.2f} RS'.format(preço, desconto, ))
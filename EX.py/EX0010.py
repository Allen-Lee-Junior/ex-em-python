real = float(input('Quanto dinheiro voce tem na carteira?:'))
Dolar = real / 5.34
Renminbi = real / 0.81
Eurofrançes = real / 6.35
EuroPortugal = real / 6.35
Libras = real / 7.13
peso = real / 15.17
print('com {} RS$ voce compra US${:.2f}'.format(real, Dolar, ))
print('com {} RS$ voce compra 人民币{:.2f}'.format(real, Renminbi, ))
print('com {} RS$ voce compra €{:.2f}'.format(real, Eurofrançes))
print('com {} RS$ voce compra €{:.2f}'.format(real, EuroPortugal, ))
print('com {} RS$ voce compra £{:.2f}'.format(real, Libras, ))
print('com {} RS$ voce compra ${:.2f}'.format(real, peso, ))
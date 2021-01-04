distacia = float(input('Qual é a distacia da sua pasagen:'))
print('Você estar prestes a comesar uma viagem de {}km'.format(distacia))
'''if distacia <=200:
    preço = distacia * 0.50
else:
    preço = distacia * 0.45'''
preço = distacia*0.50 if distacia <=200 else distacia * 0.45
print('e o preço da sua pasagem sera de {:.2f}'.format(preço))
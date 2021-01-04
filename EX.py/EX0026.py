FRA = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} na frase.'.format(FRA.count('A')))
print('A primeira letra A aparece na posição {}'.format(FRA.find('A')+1))
print('A ultima letra A aprece na posição {}'.format(FRA.rfind('A')+1))
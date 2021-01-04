dia = int(input('quantos dias alugados?'))
kilom = float(input('quantos km rodados?'))
di = dia*60
km =kilom*0.15
total = di+km
print('O total a pagar é de R${:.2f}'.format(total,))
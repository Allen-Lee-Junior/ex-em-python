SALARIO = float(input('Qual é  salario do fucionario? R$'))


if SALARIO <= 1250:
    aumento = SALARIO +(SALARIO * 15 / 100)
else:
    aumento = SALARIO + (SALARIO * 10 / 100)
print(' Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(SALARIO,aumento))
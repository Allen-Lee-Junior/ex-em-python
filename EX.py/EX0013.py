salario = float(input('Qual é o salario do funcionario? R$'))
SAL2 = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f},com 15% de aumento , passa a receber {:.2f} '.format(salario, SAL2, ))
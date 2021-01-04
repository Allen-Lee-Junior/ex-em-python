velocidade = float(input('Qual é a velocidade do veiculo?'))

if velocidade >=80:
    print('Multado!VOCÊ EXEDEU O LIMITE DE VELOCIDADE QUA É DE QUE É DE 80KM/H')
    limite = (velocidade - 80) * 7
    print('VOCÊ DEVE PAGAR UMA MUTA DE {:.0f} R$'.format(limite))

print('Tenha um Bom dia! dirija com segurança!')
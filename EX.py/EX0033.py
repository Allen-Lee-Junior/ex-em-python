a = int(input('PRIMEIRO VALOR:'))
b = int(input('SEGUNDO VALOR:'))
c = int(input('tERCEIRO VALOR:'))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
# Verificando quem é o maio
maio = a
if b > a and b > c:
    maio = b
if c > a and c > b:
    maio = c
print('O maior valor digitado foi {}'.format(maio))
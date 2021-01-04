from random import randint
from time import sleep

computador = randint(0,5 )  # FAS O COMPUTADOR "PENSAR"

print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5. temte adivinhar')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))  # O JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')

sleep(3)
if jogador == computador:
    print('PARABENS!  voce conseguiu me vencer!')
else:
    print('Ganhei! eu pensei no número {} e não no {}!'.format(computador, jogador))
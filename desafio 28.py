'''import random
print ('Vou pensar em um numero de 0 a 5, tente advinhar...')
num = int(input('Em que número eu pensei?'))
lista = random.randint(0, 5)
print ('PROCESSANDO...')
if num == lista:
    print ('PARABÉNS VOCE ACERTOU!')
else:
    print ('GANHEI! eu pensei no número {} e não no {}'.format(lista, num))'''

import random
import time
lista = random.randint (0, 100)
print ('-=-' * 20)
print ('Vou pensar em um numero de 0 a 5, tente advinhar...')
print ('-=-' * 20)
num = int(input('Em que número eu pensei?'))
print ('PROCESSANDO...')
time.sleep(3)
if num == lista:
    print ('PARABÉNS VOCE CONSEGUIU ME VENCER!!')
else:
    print ('GANHEI! eu pensei no número {} e não no {}'.format(lista, num))

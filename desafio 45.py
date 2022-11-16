from random import randint
import time
jok = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)

print ('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada?'))

print ('JO')
time.sleep(1)
print ('KEN')
time.sleep(1)
print ('PO!!!')

print ('=-' * 11)
print ('Computador jogou {}'.format(jok[pc]))
print ('Jogador jogou {}'.format(jok[jogador]))
print ('=-' * 11)

if pc == 0:
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print ('JOGADOR VENCE')
    elif jogador == 2:
        print ('COMPUTADOR VENCE')
elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif pc == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
else:
    print('JOGADA INVALIDA')









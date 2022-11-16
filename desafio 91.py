from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Valores Sorteados:')
sleep(0.3)
for k, v in jogo.items():
    print(f'  O {k} tirou {v}')
    sleep(0.8)
print('Ranking dos Jogadores:')
sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  {i+1}° Lugar: {v[0]} com {v[1]}')
    sleep(0.8)

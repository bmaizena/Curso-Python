def ficha(jogador='desconhecido', gols=0):
    print(f'o jogador {jogador} fez {gols} gol(s) no campeonato.')


j = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)



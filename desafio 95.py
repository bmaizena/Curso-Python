dados = {}
partidas = []
all = []
while True:
    dados['jogador'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}: ')))
        dados['gols'] = partidas[:]
        dados['total'] = sum(partidas)
    all.append(dados.copy())
    partidas.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!, digite somente com S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('COD', end=' ')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for i, p in enumerate(all):
    print(f'{i:>3}', end=' ')
    for d in p.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    mos = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if mos == 999:
        break
    if mos >= len(all):
        print(f'ERRO! Não existe jogador com código {mos}!')
    else:
        print(f'- LEVANTAMENTO DO JOGADOR {all[mos]["jogador"]}')
        for i, j in enumerate(all[mos]['gols']):
            print(f'  no jogo {i+1} ele fez {j} gols')
    print('-'*40)
print('<<<<VOLTE SEMPRE>>>>')


dados = {}
partidas = []
soma = 0
dados['jogador'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
for c in range(0, tot):
    gols = int(input(f'Quantos gols na partida {c}: '))
    partidas.append(gols)
    dados['gols'] = partidas
    soma += gols
    dados['total'] = soma
print('-'*30)
print(dados)
print('-'*30)
for k, v in dados.items():
    print(f'o campo {k} tem o valor {v}')
print('-'*30)
print (f'o jogador {dados["jogador"]} jogou {tot} partidas.')
for i, p in enumerate(partidas):
    print(f'   =>Na partida {i}, fez {p} gols.')
print(f'Foi um total de {dados["total"]}')
galera = []
pessoas = {}
cont = 0
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! por favor digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO responda somente com N ou S.')
    if resp == 'N':
        break
print(f' - o grupo tem {len(galera)} pessoas')
media = soma / len(galera)
print(f' - a media de idade é de {media:.2f}')
print(' - As mulheres cadastradas foram:', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print(' - Lista de pessoas que estão acima da média: ')
print()
for c in galera:
    if c['idade'] >= media:
        print(f'- Nome = {c["nome"]}; sexo = {c["sexo"]}; Idade = {c["idade"]}')
print()


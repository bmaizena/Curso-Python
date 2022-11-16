pessoas = []
dado = []
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso Kg:')))
    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('quer continuar? [S/N]')).upper()
    if resp == 'N':
        break
print(f'foram cadastradas {len(pessoas)} pessoas')
print (f'o maior peso foi de {mai}Kg. Peso de', end= ' ')
for p in pessoas:
    if p[1] == mai:
        print (f'[{p[0]}]', end= ' ')
print()
print (f'o menor peso foi de {men}Kg. Peso de', end= ' ')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end= ' ')
print()


'''lista = list()
mai = men = 0
for v in range(0, 5):
    lista.append(int(input(f'Digite um numero para a posiçao {v}: ')))
    if v == 0:
        mai = men = lista[v]
    else:
        if lista[v] > mai:
            mai = lista[v]
        if lista[v] < men:
            men = lista[v]
print(f'os valores digitados foram {lista}')
print(f'o menor valor digitado foi {men} nas posições', end=' ')
for i, p in enumerate(lista):
    if p == men:
        print (f'{i}...', end='')
print()
print(f'o maior valor digitado foi {mai} nas posições', end =' ')
for i, p in enumerate(lista):
    if p == mai:
        print (f'{i}...',end='')'''


lista = list()
for v in range(0, 5):
    lista.append(int(input(f'Digite um numero para a posiçao {v}: ')))
    mai = max(lista)
    men = min(lista)
print(f'os valores digitados foram {lista}')
print(f'o menor valor digitado foi {men} nas posições', end=' ')
for i, p in enumerate(lista):
    if p == men:
        print (f'{i}...', end='')
print()
print(f'o maior valor digitado foi {mai} nas posições', end =' ')
for i, p in enumerate(lista):
    if p == mai:
        print (f'{i}...',end='')

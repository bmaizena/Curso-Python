n = [[],[]]
for p in range(1, 8):
    lista = int(input(f'Digite o {p}° valor: '))
    if lista % 2 == 0:
        n[0].append(lista)
    elif lista % 2 == 1:
        n[1].append(lista)
n[0].sort()
n[1].sort()
print(f'os valores pares digitados foram {n[0]}')
print(f'os valores impares digitados foram {n[1]}')
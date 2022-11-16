matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print (f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'a soma de todos os valores pares é {spar}')
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'a soma dos valores da terceira coluna é {soma}')
mai = max(matriz[1])
print (f'o maior valor da segunda linha é {mai}')

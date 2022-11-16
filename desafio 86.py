'''matriz = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
valor = (int(input(f'Digite um valor para [0, 0]:')),
int(input(f'Digite um valor para [0, 1]:')),
int(input(f'Digite um valor para [0, 2]:')),
int(input(f'Digite um valor para [1, 0]:')),
int(input(f'Digite um valor para [1, 1]:')),
int(input(f'Digite um valor para [1, 2]:')),
int(input(f'Digite um valor para [2, 0]:')),
int(input(f'Digite um valor para [2, 1]:')),
int(input(f'Digite um valor para [2, 2]:')))
matriz[0][0] = valor[0]
matriz[0][1] = valor[1]
matriz[0][2] = valor[2]
matriz[1][0] = valor[3]
matriz[1][1] = valor[4]
matriz[1][2] = valor[5]
matriz[2][0] = valor[6]
matriz[2][1] = valor[7]
matriz[2][2] = valor[8]
for p in matriz:
    print (f'[{p[0]:^5}]', end='')
    print (f'[{p[1]:^5}]', end='')
    print (f'[{p[2]:^5}]', end='')
    print()'''


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
for l in range(0, 3):
    for c in range(0, 3):
        print (f'[{matriz[l][c]:^5}]', end='')
    print()


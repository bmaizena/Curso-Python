pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
cont = 9 * r + pt
for c in range(pt, cont + r, r):
    print(c, end='-> ')
print ('ACABOU')

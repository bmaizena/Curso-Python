from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
maior = menor = 0
cont = 0
print('Os Numeros Sorteados foram:', end= ' ')
for n in tupla:
    print (n, end= ' ')

print (f'\no maior valor sorteado foi {max(tupla)}')
print (f'o menor valor sorteado foi {min(tupla)}')
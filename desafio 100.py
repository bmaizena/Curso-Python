from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for num in range(1, 6):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='')
        sleep(0.3)
    print('PRONTO')


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)

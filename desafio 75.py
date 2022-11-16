'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
numeros = (n1, n2, n3, n4)'''

n = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')),
    int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
print (f'Voce digitou os valores {n}')
print (f'o numero 9 apareceu {n.count(9)} vezes')
if 3 not in n:
    print(f'O valor 3 nao foi digitado em nenhuma posição')
else:
    print(f'o valor 3 foi digitado na {(n.index(3) + 1)}ª posiçao')
print(f'os valores pares digitados foram', end=' ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')


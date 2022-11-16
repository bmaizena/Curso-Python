n = list()
par = list()
impar = list()
while True:
    num = int(input('Digite um numero: '))
    n.append(num)
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)
    resp = str(input('quer continuar? [S/N]')).upper()
    if resp == 'N':
        break
print (f'os valores digitados foram {n}')
print (f'os valores pares digitados foram {par}')
print (f'os valores impares digitados foram {impar}')




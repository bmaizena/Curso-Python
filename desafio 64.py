'''n = 0
c = 0
cont = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]:'))
    c += n
    cont += 1
print ('Voce Digitou {} números e a soma entre eles foi {}'.format((cont - 1), (c - 999)))'''

n = cont = c = 0
n = int(input('Digite um numero [999 para parar]:'))
while n != 999:
    c += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]:'))
print ('Voce Digitou {} números e a soma entre eles foi {}'.format(cont, c ))


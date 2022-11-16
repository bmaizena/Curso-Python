n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os segmentos acima FORMAM um triângulo',end=' ')
    if n1 != n2 != n3 != n1:
        print('ESCALENO')
    elif n1 == n2 == n3:
        print ('EQUILÁTERO')
    else:
        print ('ISÓSCELES')
else:
    print ('Os segmentos acima NÃO FORMAM um triângulo')
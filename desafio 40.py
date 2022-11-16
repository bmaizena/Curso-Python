n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2) / 2
if m < 5:
    print ('sua média foi de {}'.format(m))
    print('REPROVADO!')
elif m >= 5 and m <=6.9:
    print ('sua média foi de {}'.format(m))
    print ('RECUPERÇÃO!')
else:
    print ('sua média foi de {}'.format(m))
    print ('APROVADO')
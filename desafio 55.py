maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print ('o maior peso lido foi {}Kg'.format(maior))
print ('o menor peso lido foi {}Kg'.format(menor))
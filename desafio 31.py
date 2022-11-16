km = float(input('Qual a distancia de sua viagem? '))
print ('Voce esta prestes a começar uma viagem de {}km'.format(km))
if km <=199:
    print ('E o preço de sua passagem será de R${}'.format(km * 0.50))
else:
    print ('E o preço de sua passagem será de R${}'.format(km * 0.45))

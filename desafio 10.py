num = float(input('Quanto dinheiro você tem em sua carteira? R$'))
dol = (num/5.29)
euro = (num/5.28)
won = (num/0.0038)
print ('com R${} voce pode comprar U${:.2f} ou €{:.2f} ou {:.2f}won'.format(num, dol, euro, won))

'''num = float(input('Quanto dinheiro você tem em sua carteira? U$'))
dol = (num*5.29)
print ('com U${} voce pode comprar R${:.2f}'.format(num, dol))'''
dias = int(input('Quantos dias alugado? '))
km = float(input('quantos quilometros rodados? '))
total = (dias * 60) + (km * 0.15)
print ('o total a a pagar é de R${:.2f}'.format(total))
casa = float(input('Qual o valor da casa ? R$'))
sal = float(input('Qual o seu salario? R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = casa / (anos * 12)
x = (sal * 0.3)
print ('para pegar uma casa de \033[32mR${:.2f}\033[m em \033[36m{} anos\033[m a prestacão será de \033[32mR${:.2f}\033[m'.format(casa, anos, prest))
if prest < x:
    print ('EMPRÉSTIMO CONCEDIDO')
else:
    print ('EMPRÉSTIMO NEGADO')


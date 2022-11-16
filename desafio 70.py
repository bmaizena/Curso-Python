soma = pro1000 = cont = precobarato = 0
probarato = ''
print('-' *28)
print ('     LOJA SUPER BIGTEC')
print ('-'*28)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    soma += preco
    cont += 1
    if preco > 1000:
        pro1000 += 1
    if cont == 1 or preco < precobarato:
        precobarato = preco
        probarato = produto
    '''else:
        if preço < preçobarato:
            preçobarato = preço
            probarato = produto'''
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print ('{:-^40}'.format('FIM DO PROGRAMA'))
print (f'O total da compra foi de R${soma}')
print (f'Temos {pro1000} produtos custando mais de R$1000.00')
print (f'O produto mais barato foi a {probarato} que custa R${precobarato}')

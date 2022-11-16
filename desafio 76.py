print ('-'*40)
print (f'{"LISTAGEM DE PREÇOS":^40}')
print ('-'*40)

lista = ('lapis', 2.00, 'borracha', 1.50, 'caneta', 4.50, 'estojo', 20.75,
         'mochila', 150.00, 'caderno', 43.50, 'esquadro', 8.00, 'marcapasso', 5.70, 'grifatexto', 7.00)
for n in range(0, 18):
    if n % 2 == 0:
        print (f'{lista[n]:.<30}', end='')
    else:
        print (f'R$ {lista[n]:>7.2f}')
print('-'*40)

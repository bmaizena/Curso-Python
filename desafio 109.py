from uteis.utlidades import moedas

num = float(input('Digite o preço: R$'))
print(f'O dobro de {moedas.moeda(num)} é {moedas.dobro(num, True)}')
print(f'A metade de {moedas.moeda(num)} é {moedas.metade(num, True)}')
print(f'Aumentando 18% de {moedas.moeda(num)} temos {moedas.aumentar(num, 18,True)}')
print(f'Diminuindo 18% de {moedas.moeda(num)} temos {moedas.diminuir(num, 18, True)}')
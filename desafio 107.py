from uteis.utlidades import moedas

num = float(input('Digite o preço: R$'))
print(f'O dobro de {num} é {moedas.dobro(num)}')
print(f'A metade de {num} é {moedas.metade(num)}')
print(f'Aumentando 18%, temos {moedas.aumentar(num, 18):.2f}')
print(f'Diminuindo 18%, temos {moedas.diminuir(num, 18):.2f}')
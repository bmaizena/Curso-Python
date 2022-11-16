from uteis.utlidades import moedas

num = float(input('Digite o preço: R$'))
print(f'O dobro de {moedas.moeda(num)} é \033[31m{moedas.moeda(moedas.dobro(num))}\033[m')
print(f'A metade de {moedas.moeda(num)} é \033[32m{moedas.moeda(moedas.metade(num))}\033[m')
print(f'Aumentando 18%, temos \033[36m{moedas.moeda(moedas.aumentar(num, 18))}\033[m')
print(f'Diminuindo 18%, temos \033[34m{moedas.moeda(moedas.diminuir(num, 18))}\033[m')
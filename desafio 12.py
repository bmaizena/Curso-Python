
price = float(input('Qual o valor do seu produto?R$'))
desconto = price - (10/100 * price)
print  ('o produto que custava R${}, com 10% de desconto ira ficar por R${}!'.format(price, desconto))

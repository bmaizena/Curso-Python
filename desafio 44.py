print ('\033[7;31;40m{:=^40}\033[m'.format(' LOJAS SALLESSE '))
valor = float(input('Preço das compras: R$'))
print ('''FORMAS DE PAGAMENTO:
[1] à vista em dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão sem juros
[4] 3x ou mais no cartão ('possui 20% juros')''')
opçao = int(input('Qual a opção?'))
if opçao == 1:
    print (' sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor - (valor * 0.1)))
elif opçao == 2:
    print(' sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor - (valor * 0.05)))
elif opçao == 3:
    print(' sua compra de R${:.2f} vai ser parcelada em 2 vezes no valor de  R${:.2f}.'.format(valor, valor / 2))
elif opçao == 4:
    tot = int(input('Quantas Parcelas?'))
    juros = valor + (valor * 0.2)
    parcela = juros / tot
    print ('sua compra será parcelada em {} vezes de R${:.2f} COM JUROS'.format(tot, parcela))
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, juros))
else:
    print ('\033[31mOPÇÃO INVÁLIDA\033[m')
sal = float(input('Qual o salàrio do funcionàrio? R$'))
aum = sal + (0.15*sal)
print ('um funcionario que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, aum))
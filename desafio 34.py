sal = float(input('Qual o salario do funcionario? R$'))
if sal >=1250:
    print('Quem ganhava R${}, passará a ganhar R${}'.format(sal, (sal * 0.1) + sal))
else:
    print('Quem ganhava R${}, passará a ganhar R${}'.format(sal, (sal * 0.15) + sal))
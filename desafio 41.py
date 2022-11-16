from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
nas = atual - ano
print ('O atleta tem {} anos.'.format(nas))
if nas <= 9:
    print('Classificação: MIRIM')
elif nas <= 14:
    print('Classificação: INFANTIL')
elif nas <= 19:
    print ('Classificação: JUNIOR')
elif nas <=25:
    print ('Classificação: SÊNIOR')
else:
    print ('Classificação: MASTER')

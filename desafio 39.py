from datetime import date
ano = int(input('Ano de Nascimento? '))
atual = date.today().year
nasc = (atual - ano)
print ('Quem nasceu em {} tem {} anos em {}'.format(ano, nasc, atual))
if nasc < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - nasc))
    print ('Seu alistamento será em {}'.format(18 - nasc + atual))
elif nasc > 18:
    print ('Ja deveria ter se alistado há {} anos!'.format(nasc - 18))
    print ('Seu alistamento foi em {}'.format(18 - nasc + atual))
else:
    print ('Voce Precisa se alistar IMEDIATAMENTE!')
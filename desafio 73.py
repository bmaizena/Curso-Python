
times = ('palmeiras', 'internacional', 'fluminense', 'flamengo', 'corinthians',
         'athletico-pr', 'atletico-mg', 'america-mg', 'santos', 'goias', 'sao paulo',
         'botafogo', 'bragantino', 'fortaleza', 'ceara', 'coritiba', 'avai', 'cuiaba',
         'atletico-go', 'juventude')
print (f'Lista de Times: {times}')
print('-=' * 45)
print (f'os primeiros sao: {times[0:4]}')
print ('-=' * 45)
print(f'os ultimos sao: {times[-4:]}')
print ('-=' * 45)
print (f'em ordem alfabética: {sorted(times)}')
print ('-=' * 45)
print (f'o Botafogo esta na {times.index("botafogo")+1}ª posição')

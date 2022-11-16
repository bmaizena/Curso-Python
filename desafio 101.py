def voto(num):
    from datetime import date
    atual = date.today().year
    ano = atual - num
    print(f'com {ano} anos: ', end='')
    if ano >= 18:
        print('VOTO OBRIGATÓRIO.')
    elif 16 <= ano < 18 or ano > 65:
        print('VOTO OPCIONAL.')
    else:
        print('NÃO VOTA.')


print('-' * 30)
n = int(input('Em que ano você nasceu? '))
voto(n)




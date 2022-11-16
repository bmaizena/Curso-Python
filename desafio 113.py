def leiaInt(num):
    while True:
        try:
            nume = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número inteiro válido.\033[m')
            continue
        else:
            return nume




def leiaFloat(num):
    while True:
        try:
            nume = float(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('o usuario preferiu nao digitar esse numero')
            return 0
        else:
            return nume





n = leiaInt('Digite um numero inteiro: ')
f = leiaFloat('Digite um numero Real: ')
print(f'voce digitou o numero inteiro {n} e numero real {f}')
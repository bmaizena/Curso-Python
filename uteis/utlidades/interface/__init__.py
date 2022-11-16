def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(f'\033[1m{txt}\033[m'.center(50))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c} - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mSua Opção: \033[m')
    return opc
from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'      # 6 - branco
     )


def sistema(str, cor=0):
    tam = len(str) + 4
    print(c[cor], end='')
    print('°' * tam)
    print(f'  {str}')
    print('°' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    sistema('acessando o manual do comando', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


comando = ''
while True:
    sistema('SISTEMA DE AJUDA PYHELP', 2)
    print(c[5], end='')
    comando = str(input('Função ou biblioteca > '))
    print(c[0], end='')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
sistema('ATÉ LOGO', 1)
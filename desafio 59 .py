from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
menu = 0
while menu != 5:
    print('''      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NUMEROS
      [5] SAIR DO PROGRAMA''')
    menu = int(input('>>>>>Qual é sua opção?'))
    print('=-=-=-=-=-=-=-==-=-')
    soma = n1 + n2
    multi = n1 * n2
    if menu == 1:
        print('\033[31ma soma entre {} + {} é {}\033[m'.format(n1, n2, soma))
    elif menu == 2:
        print('\033[32ma multiplicação entre {} * {} é {}\033[m'.format(n1, n2, multi))
    elif menu == 3:
        if n1 > n2:
            print('\033[33mo numero {} é maior que o numero {}\033[m'.format(n1, n2))
        elif n2 > n1:
            print ('\033[34mo numero {} é maior que o numero {}\033[m'.format(n2, n1))
        else:
            print('\033[36mos dois numeros digitados sao iguais\033[m')
    elif menu == 4:
        soma = n1 + n2
        multi = n1 * n2
        print('\033[4minforme os numeros novamente: \033[m')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == 5:
        print ('Finalizando...')
    else:
        print ('\033[7;30;41mOPÇÃO INVALIDA, TENTE NOVAMENTE\033[m')
    sleep(1.5)
print('FIM DO PROGRAMA, VOLTE SEMPRE')
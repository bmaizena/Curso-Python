'''from time import sleep
def maior(*valores):
    print('\033[31mº\033[m' * 30)
    print('Analisando os valores passados...')
    sleep(2)
    for c in valores:
        print(f'{c} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {max(valores)}.')'''


from time import sleep
def maior(*valores):
    cont = mai = 0
    print('\033[31mº\033[m' * 30)
    print('Analisando os valores passados...')
    sleep(2)
    for c in valores:
        print(f'{c} ', end='')
        sleep(0.5)
        cont +=1
        if cont == 0:
            mai = c
        else:
            if c > mai:
                mai = c
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {mai}.')


maior(3, 50, 7, 3, 1, 9)
maior(4, 6, 7, 2, 1)
maior()
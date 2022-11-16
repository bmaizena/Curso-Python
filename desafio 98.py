from time import sleep
def contador(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print (i, end=' ')
        sleep(0.4)
    print('FIM')
    print('-='*30)


print('-='*30)
print('\033[31mContagem de 1 até 10 de 1 em 1\033[m')
sleep(0.5)
contador(1, 11, 1)
print('\033[33mContagem de 10 até 0 de 2 em 2\033[m')
sleep(0.5)
contador(10, -1, -2)
print('\033[36mAgora é sua vez de personalizar a contagem!\033[m')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
if passo < 0:
    passo *= -1
print('-='*30)
print(f'\033[36mcontagem de {inicio} ate {fim} de {passo} em {passo}\033[m')
sleep(0.5)
if fim < inicio:
    passo = - passo
fim += passo
contador(inicio, fim, passo)


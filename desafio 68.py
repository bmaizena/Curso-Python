import random
print ('-='*15)
print ('VAMOS JOGAR PAR OU ÍMPAR')
print ('-='*15)
v = 0
while True:
    n = int(input('Diga um valor: '))
    pc = random.randint(0, 10)
    soma = n + pc
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I]: ')).upper()
    print(f'voce jogou {n} e o computador jogou {pc}. Total de {soma}', end = ' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if pi == 'P':
        if soma % 2 == 0:
            print ('VOCE GANHOU!')
            v +=1
        else:
            print ('VOCE PERDEU')
            break
    elif pi == 'I':
        if soma % 2 == 1:
            print ('VOCE GANHOU')
            v += 1
        else:
            print ('VOCE PERDEU')
            break
    print ('Vamos jogar novamente...')
print (f'GAME OVER!, Voce Venceu {v} vezes')


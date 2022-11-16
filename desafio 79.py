n = []
while True:
    num = int(input('Digite um valor:'))
    if num not in n:
        n.append(num)
        print('valor adicionado com sucesso')
    else:
        print('valor duplicado, nao vou adicionar')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper()
    if resp in 'N':
        break
n.sort()
print (n)
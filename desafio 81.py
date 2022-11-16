n= []
while True:
    n.append(int(input('Digite um valor? ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
n.sort(reverse=True)
print ('-='*30)
print (f'foram digitados {len(n)} numeros')
print (f'a ordem descrescente dos numeros fica {n}')
if n.count(5):
    print('o numero 5 esta na lista!')
else:
    print('o numero 5 nao esta na lista')

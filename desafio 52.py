num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print (c, end=' ')
print ('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print ('E por isso ele é PRIMO!')
else:
    print ('E por isso ele NÃO É PRIMO!')



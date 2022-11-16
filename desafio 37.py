num = int(input('digite um numero inteiro: '))
print ('''Escolha uma das bases de conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print ('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print ('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente')


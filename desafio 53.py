frase = str(input('Digite uma Frase: ')).strip().upper()
fr = frase.split()
frx = ''.join(fr)
inverso = frx[::-1]
'''inverso = ''
for letra in range(len(frx) - 1, -1, -1):
    inverso = inverso + frx[letra]'''
print('O inverso de {} é \033[31m{}\033[m'.format(frx, inverso))
if frx == inverso:
    print ('A frase digitada é um palindromo!')
else:
    print ('A frase digitada não é um palindromo')


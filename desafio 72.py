cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    numeros = int(input('digite um numero entre 0 e 20: '))
    if numeros >=0 and numeros <=20:
        print(f'voce digitou o numero {cont[numeros]}')
    else:
        print ('Tente Novamente')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer digitar outro numero entre 0 a 20: [S/N] ')).upper()
    if resp == 'N':
        break
print('fim')
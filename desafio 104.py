def leiaInt(num):
    while True:
        nume = str(input(num))
        if nume.isnumeric():
            return nume
        else:
            print('\033[0;31mERRO!! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um numero inteiro: ')
print(f'voce digitou o valor {n}')
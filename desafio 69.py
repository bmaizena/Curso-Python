print ('CADASTRE UMA PESSOA')
totmais = 0
homens = 0
mulhermenos = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper()
        if idade >= 18:
            totmais += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulhermenos += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('quer continuar: [S/N]')).upper()
    if continua == 'N':
        break
print (f'Total de pessoa com mais de 18 anos: {totmais}')
print (f'o todo temos {homens} homens cadastrados')
print (f'e temos {mulhermenos} mulheres com menos de 20 anos')
lista = {}
lista['Nome'] = str(input('Nome: '))
lista['Média'] = float(input(f'Média de {lista["Nome"]}: '))
if lista['Média'] >= 7:
    lista['Situação'] = 'Aprovado'
elif 5 <= lista['Média'] < 7:
    lista['Situação'] = 'Recuperação'
else:
    lista['Situação'] = 'Reprovado'
for k, v in lista.items():
    print(f'{k} é igual a {v}')
from datetime import date
atual = date.today().year
inf =  {}
inf['Nome'] = str(input('Nome: '))
inf['Idade'] = atual - int(input('Ano de nascimento: '))
inf['Ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if inf['Ctps'] != 0:
    inf['Contratação'] = int(input('Ano de contratação: '))
    inf['salario'] = float(input('Salario: R$'))
    inf['Aposentadoria'] = inf['Contratação'] + 35 - atual + inf['Idade']
print('-='* 30)
for k, v in inf.items():
    print(f'  - {k} tem o valor {v}')
print (inf)

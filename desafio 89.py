lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp in 'N':
        break
print('-='* 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print ('-'* 26)
for i, n in enumerate(lista):
    print (f'{i:<4} {n[0]:<10}{n[2]:>8}')
print('-'*30)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 para parar)'))
    if mostrar == 999:
        print('FINALIZANDO')
        break
    if mostrar <= len(lista) -1:
        print(f'as notas de {lista[mostrar][0]} sao {lista[mostrar][1]}')
        print('-'* 30)
print('VOLTE SEMPRE')
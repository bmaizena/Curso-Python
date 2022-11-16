print ('   GERADOR DE PA')
print ('=-' * 10)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
cont = 0
soma = pt
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont != total:
        print('{} ->'.format(soma), end=' ')
        soma += r
        cont += 1
    print ('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar mais? '))
print ('FIM')
print ('PROGRESSÃO FINALIZADA COM {} TERMOS MOSTRADOS'.format(cont))







sn = 'SsNn'
cont = media = soma = maior = menor = 0
while sn != 'N':
    n = int(input('Digite um numero:'))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    sn = str(input('Quer continuar?[S/N]')).upper()
media = soma/cont
print ('voce digitou {} numeros e a media foi {:.2f}'.format(cont, media))
print (f'O maior valor foi {maior} e o menor {menor}')
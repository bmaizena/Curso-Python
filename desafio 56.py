soma = 0
media = 0
maiorhomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print ('------{}ª PESSOA------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    soma = soma + idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = soma/4
print ('a média de idade do grupo é de {} anos'.format(media))
print ('o homem mais velho tem {} anos e se chama {}.'.format(maiorhomem, nomevelho))
print ('ao todos sao {} mulheres com menos de 20 anos'.format(totmulher20))

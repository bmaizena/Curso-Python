import random
print ('Sou seu computador...')
print ('Acabei de pensar em numero entre 0 e 10.')
print ('Sera que voce consegue advinhar qual foi?')
lista = random.randint (0, 10)
cont = 1
palpite = int(input('Qual é o seu palpite?'))
while palpite != lista:
    if palpite > lista:
        print ('Menos... Tente de novo')
        palpite = int(input('Qual é o seu palpite?'))
        cont += 1
    elif palpite < lista:
        print ('Mais... Tente de novo')
        palpite = int(input('Qual é o seu palpite?'))
        cont += 1
print ('voce acertou com {} tentativas, PARABÉNS!'.format(cont))



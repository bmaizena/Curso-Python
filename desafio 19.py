import random
pri = input('Primeiro Aluno?')
seg = input('Segundo Aluno?')
ter = input ('Terceiro Aluno?')
qua = input('Quarto Aluno?')
lista = [pri, seg, ter, qua]
sort = random.choice(lista)

print ('o aluno escolhido foi {}'.format(sort))

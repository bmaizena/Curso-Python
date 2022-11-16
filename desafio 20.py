import random
pri = input('Primeiro Aluno?')
seg = input('Segundo Aluno?')
ter = input ('Terceiro Aluno?')
qua = input('Quarto Aluno?')
lista = [pri, seg, ter, qua]
random.shuffle(lista)

print (' a ordem de apresetaçao sera')
print (lista)

nome = (input('Qual seu nome ? ')).strip()
print ('analisando nome...')
print ('seu nome em maisculo fica {}'.format(nome.upper()))
print ('seu nome em minusculo fica {}'.format(nome.lower()))
print ('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print ('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print ('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


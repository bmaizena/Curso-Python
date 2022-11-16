from uteis.utlidades import interface
from uteis.utlidades.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)
    elif resposta == 3:
        interface.cabecalho('Saindo do Sistema... Até Logo')
        break
    else:
        print('\033[1;31mERRO!, Digite uma opção válida\033[m')
    sleep(2)


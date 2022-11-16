from uteis.utlidades.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a =open(nome, 'wt+')
        a.close()
    except:
        print('houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<10}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastro(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

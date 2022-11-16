def aumentar(num, taxa=0, formato=False):
    aum = num + (num * taxa/100)
    return aum if formato is False else moeda(aum)


def diminuir(num, taxa=0, formato=False):
    dim = num - (num * taxa/100)
    return dim if formato is False else moeda(dim)


def metade(num, formato=False):
    met = num / 2
    return met if formato is False else moeda(met)


def dobro(num, formato=False):
    dob = num * 2
    return dob if formato is False else moeda(dob)


def moeda(num=0, cif='R$'):
    return f'{cif}{num:.2f}'.replace('.', ',')


def resumo(num, aum=10, dim=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado:  \t{moeda(num)}')
    print(f'Dobro do Preço:  \t{dobro(num, True)}')
    print(f'Metade do Preço:  \t{metade(num, True)}')
    print(f'{aum}% de Aumento:  \t{aumentar(num, aum, True)}')
    print(f'{dim}% de Redução:  \t{diminuir(num, dim, True)}')
    print('-'*30)



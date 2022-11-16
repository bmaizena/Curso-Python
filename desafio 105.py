def notas(*num, sit=False):
    dados = {}
    media = (sum(num)) / len(num)
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['media'] = (f'{media:.2f}')
    if sit:
        if media >= 7:
            dados['situaçao'] = 'BOA'
        if media >= 5:
            dados['situaçao'] = 'RAZOAVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados



resp = notas(5.5, 6.3, 1.4, 4.9, 2.5, 5.1, 4.9, 9.1, 8.5, 1.9, sit=True)
print(resp)

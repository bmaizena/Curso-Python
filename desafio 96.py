def area(l, c):
    area = l * c
    print(f'A area de um terreno {l}x{c} é de {area:.2f}m².')


print('     CONTROLE DE TERRENOS')
print('-'*30)
area(l=float(input('LARGURA (m): ')), c=float(input('COMPRIMENTO (m): ')))




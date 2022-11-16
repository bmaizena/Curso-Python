from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    ano = atual - nasc
    if ano >= 18:
        totmaior += 1
    else:
        totmenor +=1
print('ao todo tivemos {} pessoas menores de idade'.format(totmenor))
print('ao todo tivemos {} pessoas maiores de idade'.format(totmaior))


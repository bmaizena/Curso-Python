pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
ter = int(input('Terceiro valor: '))
menor = pri
if seg < pri and seg < ter:
    menor = seg
if ter < pri and ter < seg:
    menor = ter
maior = pri
if seg > pri and seg > ter:
    maior = seg
if ter > pri and ter > seg:
    maior = ter
print('o menor valor digitado foi \033[33m{}\033[m'.format(menor))
print('o maior valor digitado foi \033[31m{}'.format(maior))
print ('\033[7;30mANALISADOR DE TRIÂNGULOS\033[m')
print ('\033[1;31m-=-\033[m' * 10)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print ('Os segmentos acima FORMAM um triângulo')
else:
    print ('Os segmentos acima NÃO FORMAM um triângulo')

#a soma de qualquer segmento tem que ser menor que a soma dos outros dois segmentos para formar um triângulo
'''from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = (co**2)+(ca**2)
print ('o valor de {} ao quadrado + {} ao quadrado ira resultar no valor da hipotenusa {:.2f} ao quadrado'.format(co, ca, sqrt(hip)))'''

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
'''hip = math.hypot(co, ca)'''
print ('o valor de {} ao quadrado + {} ao quadrado ira resultar no valor da hipotenusa {:.2f} ao quadrado'.format(co, ca, math.hypot(co, ca)))


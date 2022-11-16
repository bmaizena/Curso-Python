lar = float(input('Largura da parede?'))
alt = float(input('Altura da parede?'))
s = lar * alt
m = s/2
print ('A sua parede tem a dimensao de {}x{} e sua area é de {} m2'.format(lar, alt, s))
print ('Para pintar essa parede, voce irá precisar de {}L de tinta'.format(m))
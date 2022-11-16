kg = float(input('Qual seu peso (Kg): '))
alt = float(input('Qual sua altura (m): '))
imc = kg / (alt**2)
print ('o IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <=18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print ('PARABÉNS, esta no peso normal')
elif imc <= 30:
    print ('SOBREPESO!')
elif imc <= 40:
    print ('OBESIDADE!')
else:
    print ('OBESIDADE MORBIDA')
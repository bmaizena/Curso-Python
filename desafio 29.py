km = float(input('Qual a velocidade do carro? '))
multa = (km - 80) * 7
if km > 80:
    print ('MULTADO! voce excedeu o limite permitido de que é de 80km/h')
    print ('Voce deve pagar uma multa de R${}!'.format(multa))

print ('Tenha um bom dia! dirija com cuidado!')


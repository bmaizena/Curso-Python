'''cel = float(input('Informe a temperatura em °C: '))
far = (cel*1.8 + 32)
print ('a temperatura de {}°C corresponde a {:.1f}°F'.format(cel, far))'''

far = float(input('Informe a temperatura em °F: '))
cel = (far-32) / 1.8
print ('a temperatura de {}°F corresponde a {:.1f}°C'.format(far, cel))
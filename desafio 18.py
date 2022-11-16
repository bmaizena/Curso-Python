import math
ang = float(input('digite o angulo que voce deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print ('o angulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print ('o angulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print ('o angulo de {} tem o TANGENTE de {:.2f}'.format(ang, tan))

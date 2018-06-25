#Se velocidade for > de 80Km aplicar multa de R$ 7.00 por Km adicional
vel = float(input('Qual foi a velocidade do carro (em Km)? '))
multa = (vel - 80) * 7
if vel > 80:
    print('Voce foi multado em R$ {}'.format(multa))
else:
    print('Voce NAO foi multado!')
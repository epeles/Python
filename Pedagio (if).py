vel = float(input('Qual foi a velocidade? '))
if vel <= 200:
    print('Seu pedágio foi de R$ {}'.format(vel * 0.5))
else:
    print('Seu pedágio foi de R$ {}'.format(vel * 0.45))
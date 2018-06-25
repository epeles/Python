n1 = float(input('Insira a sua 1a nota: '))
n2 = float(input('Insira a sua 2a nota: '))
m = (n1 + n2) / 2
if m <=6:
    print('Sua média foi {}. Estude mais!'.format(m))
else:
    print('Sua media foi {}. Muito bem!'.format(m))
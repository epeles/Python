n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior: {}'.format(n1))
elif n1 < n2:
    print('O segundo número é maior: {}'.format(n2))
else:
    print('Ambos sao iguais! {}'.format(n1))
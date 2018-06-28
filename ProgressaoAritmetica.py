#Exibir a sequencia de 10 numeros de uma PA:
elem = int(input('Informe o elemento da PA: '))
const = int(input('Informe a constante da PA: '))
for c in range(1, 11):
    pa = elem + (c-1) * const
    print(f'{pa}', end='-> ')
print('END')

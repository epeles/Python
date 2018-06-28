#Exibir a sequencia de 10 numeros de uma PA:
elem = int(input('Digite o elemento: '))
const = int(input('Digite a constante: '))
dez = elem + (11) * const
for c in range(elem,dez,const):
    print(f'{c}', end='-> ')
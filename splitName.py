nome = 'Eitan Menahem Peles'
maiusculo = nome.upper()
minusculo = nome.lower()
tamanho = len(nome) - nome.count(' ')
primeironome = nome.split()
print('1 - O nome dele é {}'.format(maiusculo))
print('2 - O nome dele é {}'.format(minusculo))
print('3 - Este nome tem {} caracteres'.format(tamanho))
print('4 - O primeiro nome tem {} letras'.format(len(primeironome[0])))

'''
num = input('Digite um numero de 4 dígitos: ')
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
'''
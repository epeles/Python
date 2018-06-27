soma = 0
cont = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    soma += n
for x in range(1, soma+1):
    if soma % x == 0:
        cont += 1
if cont == 2:
    primo = soma
    print(f'O número {primo} é primo')
print(f'A soma total foi de {soma} e a média foi de {soma/4}')
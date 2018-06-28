primo = 0
num = int(input('Digite o numero: '))
for c in range(1,num+1):
    if num % c == 0:
        primo += 1
if primo == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O numero {num} não é primo!')
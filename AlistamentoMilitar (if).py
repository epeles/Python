from datetime import datetime
anonasc = int(input('Ano de nascimento: '))
anoatual = datetime.now().year
idade = anoatual - anonasc
if idade < 18:
    print(f'Você ainda tem {18-idade} anos para se alistar')
elif idade == 18:
    print('Chegou a hora de você se alistar!')
else:
    print(f'Já passou da hora, você deveria ter se apresentado há {idade-18} anos')

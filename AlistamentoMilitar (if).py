from datetime import datetime
anonasc = int(input('Ano de nascimento: '))
anoatual = datetime.now().year
idade = anoatual - anonasc
if idade < 18:
    print('Você ainda tem {} anos para se alistar'.format(18-idade))
elif idade == 18:
    print('Chegou a hora de você se alistar!')
else:
    print('Já passou da hora, você deveria ter se apresentado há {} anos'.format(idade-18))
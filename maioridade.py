import datetime
anoatual = datetime.datetime.today().year
maior = 0
menor = 0
pessoas = int(input('Qts pessoas queremos comparar? '))
for c in range(1,pessoas+1):
    ano = int(input(f'Em que ano a {c}a pessoa nasceu? '))
    if anoatual - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas atingiram a maioridade')
print(f'{menor} pessoas ainda não atingiram a maioridade')
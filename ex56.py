nomejovem = 0
nomevelho = 0
maior = 0
menor = 1000
maisnova = 1000
soma = 0
jovem = 0
id = 0
qtde = int(input('Qts pessoas vc deseja comparar? '))
for c in range(1, qtde+1):
    nome = str(input(f'Digite o nome da {c}a pessoa: ')).capitalize()
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = str(input(f'Digite o sexo de {nome} (M ou F): ')).upper()
    soma += idade
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
    if idade > id and sexo == 'M':
        id = idade
        nomevelho = nome
    if idade < 20 and sexo == 'F':
        jovem += 1
    if idade < maisnova and sexo == 'F':
        nomejovem = nome
        maisnova = idade
media = soma / qtde
if sexo == 'M':
    print(f'O nome do homem mais velho é: {nomevelho}, que tem {id} anos')
if sexo == 'F':
    print(f'O número de mulheres abaixo de 20 anos é: {jovem}, sendo que a mais jovem se chama {nomejovem} e tem {maisnova} anos')
print(f'A média de idade das {qtde} pessoas: {media:.2f}')
print(f'A pessoa mais velha tem {maior} anos e a mais jovem tem {menor}')
soma = 0
jovem = 0
id = 0
qtde = int(input('Qts pessoas vc deseja comparar? '))
for c in range(1, qtde+1):
    nome = str(input(f'Digite o nome da {c}a pessoa: ')).capitalize()
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = str(input(f'Digite o sexo de {nome} (M ou F): ')).upper()
    soma += idade
    if idade > id and sexo == 'M':
        id = idade
        oldest = nome
    if idade < 20 and sexo == 'F':
        jovem += 1
media = soma / qtde
print(f'A média de idade das {qtde} pessoas: {media:.2f}')
print(f'O nome do homem mais velho é: {oldest}')
print(f'O número de mulheres abaixo de 20 anos é: {jovem}')
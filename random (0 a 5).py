from random import randint
num = randint(0, 5)
questao = float(input('Chute um numero de 0 a 5: '))
if questao == num:
    print('Acertou!')
else:
    print("Errou!")
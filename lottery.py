from random import randint
from time import sleep
def lottery(qtty):
    lista = []
    games = []
  #  qtty = int(input('How many tickets would you like to buy? '))
    for c in range(1,qtty+1):
        cont = 0
        while True:
            num = randint(1,60)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 6:
                break
        lista.sort()
        games.append(lista[:])
        lista.clear()
    for pos, number in enumerate(games):
        print(f'Ticket {pos+1}: {number}')
        sleep(1)
    print('=-'*5, 'GOOD LUCK', '=-'*5)    

lottery(5)

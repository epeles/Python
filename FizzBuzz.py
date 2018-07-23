def fizzbuzz():
    num = by3 = by5 = by15 = 0
    end = int(input('How many numbers would you like? '))
    for c in range(1,end+1):
        if c % 15 == 0:
            print('\033[31mFizz\033[34mBuzz', end=" ")
            by15 += 1
        elif c % 3 == 0:
            print('\033[31mFizz',end=" ")
            by3 += 1
        elif c % 5 == 0:
            print('\033[34mBuzz', end=" ")
            by5 += 1
        else:
            print(f'\033[0m{c}', end=" ")
    print()
    print(f'\033[0mFound {by3} numbers multiple of 3')
    print(f'Found {by5} numbers multiple of 5')
    print(f'Found {by15} numbers multiple of 3 and 5')

fizzbuzz()
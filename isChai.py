def is_chai():
    chai = []
    numbers = int(input('How many numbers would you like to know if are chai? '))
    for possibleChai in range(2, numbers+1):
        isChai = False
        for num in range(2, possibleChai):
            if possibleChai % 18 == 0:
                isChai = True
        if isChai:
            chai.append(possibleChai)
    print(chai)

is_chai()
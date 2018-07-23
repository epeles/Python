def factorial():
    fat = 1
    i = 2
    qty = int(input("Would you like to print a list of factorials from 2 until which number? "))
    for n in range(2,qty+1):
        while i <= n:
            fat *= i
            i += 1
            print(f'The factorial of {n}! is = {fat}')

factorial()
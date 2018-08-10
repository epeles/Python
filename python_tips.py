#1 - SLICE:

str[0] #first element of an array
str[-1] #last element of an array (first position from the right to the left)
str[-3] #the third position from the right to the left (ex: 'abcde' -> 'c')
str[1:] #from the second element to the end of an array
str[2:] #from the third position to the end of an array (ex: 'abcde' -> 'cde')
str[:3] #from the first element to the third element of an array (ex: 'abcde'  -> 'abc')
str[:-2] #from the first element to the second position from the right to the left (ex: 'abcde' -> 'abc')
str[-2:] #from the second position from the right to the left until the end of an array (ex: 'abcde' -> 'de')
str[1:-1] # all the elements of an array, except the first and last
str[2:-2] # from the third element to the third before the end (ex: 'abcde' -> 'c')
str[-3:-1] #from the third element before the end to the last before the end (ex: 'abcde' -> 'cd') 
str[2:4] #from the third element to the fourth position (ex: 'abcde' -> 'cd')
str[::2] #from the fist to the end, but skiping 1 element. recommended for returning even numbers (ex: 'abcdef' -> 'aceg')

=====================================================
#2 - ITERATION (FOR)

#a) Use 'for char in str:' when you want to iterate the entire array
str = 'ABCDE'
for char in str:
    print(char) #A B C D E
	
#b) Use 'for pos in range(len(str)+1): when you want to iterate the positions from the array
str = 'ABCDE'
for pos in range(len(str)+1):
    print(pos) #1 2 3 4 5

#c) Use 'for pos, stuff in enumerate(stuffs):' when you want to show the position and element from the array
stuffs = ['hello', 'world', 'hi', 'earth']
for pos, stuff in enumerate(stuffs):
    print (pos+1, stuff)
'''
1 hello
2 world
3 hi
4 earth
'''

=====================================================
#3 - CONDITIONALS

nomes = ['eitan','miriam','ilana','reinaldo','debora']
if 'eitan' in nomes:
    print(nomes[0].upper()) #EITAN
	
resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
		break #if the input is N or n, the break is activated

def love6(a, b):
  if a + b == 6 or abs(a-b) == 6 or a == 6 or b == 6:
    return True
  else:
    return False
	
#the code above is the same as below:	
 
def love6(a, b):  
  return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6		

#===============================================================
  
def lone_sum(a, b, c):
  if a == b and b == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a + b + c  

#the code above is the same as below:	
	
def lone_sum(a, b, c):
  sum = 0
  sum += a if a not in [b,c] else 0
  sum += b if b not in [a,c] else 0
  sum += c if c not in [a,b] else 0
  return sum  
  
=====================================================  
#4 - 
#min and max returns the lowest and highest element from an array

print(min(len(str1),len(str2)))	#compares 2 variables and return the lenght of the lowest between them






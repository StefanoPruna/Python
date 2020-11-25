number = input('insert a number: ')
x = int(number) 
if x > 10:
   print('x is greater than 10')
elif x < 10:
    print('x is lower than 10')
else:
    print('x is equals to 10')


age = input('Insert your age: ')
yourAge = int(age)
if yourAge <= 0:
    print(input('You cannot be serius! Insert your age again: '))
else:
    print('Your age is: ' + str(yourAge))  
         
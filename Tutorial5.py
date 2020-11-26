def factorial(n):
    """Calculate the factorial of the given value and return the result.
    the factorial of n is the product of all positive integers less than or equal to n.
    
    Arguments:
    n --A positive integer
"""
    result = 1
    while n> 0:
        for i in range(1, 4):
            n = n - 1
            result = (result * n) 
            print(result)
            return result
    print('Factorial of', i, 'is', factorial(i))
    
#Calculate factorial for the first four integers
#for i in range(1, 4):
    #print('Factorial of', i, 'is', factorial(i))

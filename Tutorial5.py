def factorial(n):
  """Calculate the factorial of the given value and return the result.

    The factorial of n is the product of all positive integers less than or equal to n.

    Arguments:
    n -- A positive integer
  """
  result = 1
  while n > 1:
    n = n - 1
    result = (n + 1) * result
    print("the result is: " + str(result))
  return result

# Calculate factorial for the first four integers
for i in range(1, 5):
  print('Factorial of', i, 'is', factorial(i))

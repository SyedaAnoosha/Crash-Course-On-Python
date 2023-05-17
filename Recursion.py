def factorial(n):
   if n < 2:
      return 1
   return n * factorial(n-1)


for n in range (1,10,1):
   print("Factorial of "+ str(n)+": "+ str(factorial(n)))

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
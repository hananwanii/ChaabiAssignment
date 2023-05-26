factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Get input from the user
num = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(num)

# Print the result
print("Factorial of", num, "is", result)

def subtract(a, b):
    c = a + (~b + 1)
    return c
num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

result = subtract(num1, num2)

print("The subtraction result is:", format(result, 'b'))

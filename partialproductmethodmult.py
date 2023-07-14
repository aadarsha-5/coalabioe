def binary_multiplication(binary1, binary2):
    # Convert binary numbers to decimal
    num1 = int(binary1, 2)
    num2 = int(binary2, 2)

    # Perform partial product multiplication
    partial_products = []
    for i, bit in enumerate(binary2[::-1]):
        if bit == '1':
            partial_product = num1 << i  # Shift num1 by the corresponding position
            partial_products.append(partial_product)

    # Calculate the final product
    result = sum(partial_products)

    # Convert the result back to binary
    binary_result = bin(result)[2:]

    return binary_result

# Prompt the user to enter the binary numbers
binary1 = input("Enter the first binary number: ")
binary2 = input("Enter the second binary number: ")

# Perform binary multiplication using the partial product method
result = binary_multiplication(binary1, binary2)

# Print the result
print("The result of multiplying", binary1, "and", binary2, "is", result)

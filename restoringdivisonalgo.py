def restoring_division(dividend, divisor):
    # Convert dividend and divisor to positive numbers
    dividend = abs(dividend)
    divisor = abs(divisor)

    # Determine the number of bits for the dividend and divisor
    dividend_bits = len(bin(dividend)) - 2
    divisor_bits = len(bin(divisor)) - 2

    # Initialize the quotient and remainder to zero
    quotient = 0
    remainder = 0

    # Perform the restoring division algorithm
    for i in range(dividend_bits):
        # Shift the quotient and remainder left by 1 bit
        quotient <<= 1
        remainder <<= 1

        # Set the least significant bit of the remainder to the next bit of the dividend
        remainder |= (dividend >> (dividend_bits - 1 - i)) & 1

        # If the remainder is greater than or equal to the divisor, subtract the divisor
        if remainder >= divisor:
            remainder -= divisor
            quotient |= 1

    # Determine the sign of the quotient based on the signs of the dividend and divisor
    if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0):
        quotient = -quotient

    # Convert the quotient and remainder to binary format
    binary_quotient = bin(abs(quotient))[2:]
    binary_remainder = bin(abs(remainder))[2:]

    return binary_quotient, binary_remainder

# Prompt the user to enter the dividend and divisor
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Perform the division using the restoring division algorithm
quotient, remainder = restoring_division(dividend, divisor)

# Print the quotient and remainder in binary format
print("Quotient (Binary):", quotient)
print("Remainder (Binary):", remainder)

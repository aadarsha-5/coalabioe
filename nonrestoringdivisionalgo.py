def non_restoring_division(dividend, divisor):
    # Initialize the quotient and remainder
    quotient = 0
    remainder = dividend

    # Check for special cases
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    if dividend == 0:
        return '0', '0'

    # Determine the sign of the quotient
    if (dividend < 0) != (divisor < 0):
        quotient = -quotient

    # Convert dividend and divisor to positive values
    dividend = abs(dividend)
    divisor = abs(divisor)

    # Perform non-restoring division
    while remainder >= divisor:
        remainder -= divisor
        quotient += 1

    # Convert the quotient and remainder to binary format
    binary_quotient = bin(abs(quotient))[2:]
    binary_remainder = bin(abs(remainder))[2:]

    return binary_quotient, binary_remainder

# Prompt the user to enter the dividend and divisor
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Perform non-restoring division
quotient, remainder = non_restoring_division(dividend, divisor)

# Display the quotient and remainder in binary format
print("Quotient (Binary):", quotient)
print("Remainder (Binary):", remainder)


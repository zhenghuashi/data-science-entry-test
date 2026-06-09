def check_divisibility(num, divisor):
    """
    Task 1
    - Check if num is divisible by divisor.
    - Both num and divisor must be numeric.
    - Return True if divisible, False otherwise.
    """

    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False

    if divisor == 0:
        return False

    return num % divisor == 0


# Task 2

# Scenario 1
result1 = check_divisibility(10, 2)
print(result1)

# Scenario 2
result2 = check_divisibility(7, 3)
print(result2)

def swap(x, y):
    """
    Task 1
    - Swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y are not numeric.
    - Print the swapped values if both x and y are numeric.
    """

    # Check if both values are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap using only x and y
    x, y = y, x

    print("Swapped values:")
    print("x =", x)
    print("y =", y)


# Task 2
# Scenario 1
result = swap("Apple", 10)
if result == -1:
    print(result)

# Scenario 2
result = swap(9, 17)
if result == -1:
    print(result)
    

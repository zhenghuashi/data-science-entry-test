def string_reverse(s):
    """
    Task 1
    - Reverse a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    if not isinstance(s, str):
        return -1

    return s[::-1]


# Task 2

# Scenario 1
result1 = string_reverse("Hello World")
print(result1)

# Scenario 2
result2 = string_reverse("Python")
print(result2)

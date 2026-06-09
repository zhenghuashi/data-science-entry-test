def update_dictionary(dct, key, value):
    """
    Task 1
    - Update a dictionary with a new key-value pair.
    - If the key already exists, print the original value,
      then update its value.
    - Return the updated dictionary.
    """

    if key in dct:
        print("Original value:", dct[key])

    dct[key] = value
    return dct


# Task 2

# Scenario 1
result1 = update_dictionary({}, "name", "Alice")
print(result1)

# Scenario 2
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)

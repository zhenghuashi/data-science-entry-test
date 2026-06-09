def find_first_negative(lst):
    """
    Task 1
    - Find the first negative number in a list.
    - Return the first negative number if found,
      otherwise return "No negatives".
    - Use a while loop.
    """

    index = 0

    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1

    return "No negatives"


# Task 2

# Scenario 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(result1)

# Scenario 2
result2 = find_first_negative([2, 10, 7, 0])
print(result2)

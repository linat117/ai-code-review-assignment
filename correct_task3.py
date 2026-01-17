# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    total = 0
    count = 0

    for v in values:
        try : 
            if v is not None:
                total += float(v)
                count += 1

        except(ValueError, TypeError):#there might be values which can't eb converted to float , that' why i use the except block here
            continue

    if count == 0:
        return 0

    return total / count
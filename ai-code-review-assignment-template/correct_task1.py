# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total=  0
    count = 0

    for order in orders:
        if orders.get("status")!= "cancelled":
            total += order.get("amount", 0) # here order.get will return None if status is missing
            count+= 1


    if count ==0:
        return 0 # this one will works when there are no valid order so it return 0 to avoid zero division error

    return total / count
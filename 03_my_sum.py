def my_sum(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)

def my_sum_recursive(list):
    return list[0] + my_sum_recursive(list[1:]) if list else 0

def my_sum_recursive2(list):
    if len(list) == 0:
        return 0
    return list[0] + my_sum_recursive2(list[1:])

# BONUS: Recursive
print(my_sum_recursive(
    [1,2,3,4.5]
))